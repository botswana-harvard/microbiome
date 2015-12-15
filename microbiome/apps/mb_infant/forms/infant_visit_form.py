from django import forms
from django.contrib.admin.widgets import AdminRadioSelect, AdminRadioFieldRenderer

from edc_constants.constants import MISSED_VISIT, OFF_STUDY, LOST_VISIT, DEATH_VISIT, YES, UNKNOWN, ALIVE, DEAD

from microbiome.apps.mb.choices import VISIT_REASON, VISIT_INFO_SOURCE
from microbiome.apps.mb_maternal.models import MaternalConsent, MaternalDeathReport

from ..models import InfantVisit

from .base_infant_model_form import BaseInfantModelForm


class InfantVisitForm(BaseInfantModelForm):

    reason = forms.ChoiceField(
        label='Reason for visit',
        choices=[choice for choice in VISIT_REASON],
        help_text="",
        widget=AdminRadioSelect(renderer=AdminRadioFieldRenderer))

    info_source = forms.ChoiceField(
        required=False,
        label='Source of information',
        choices=[choice for choice in VISIT_INFO_SOURCE],
        widget=AdminRadioSelect(renderer=AdminRadioFieldRenderer))

    def clean(self):
        cleaned_data = super(InfantVisitForm, self).clean()
        self.validate_presence()
        self.validate_reason_death()
        self.validate_reason_lost_and_completed()
        self.validate_reason_visit_missed()
        self.validate_survival_status_if_alive()
        self.validate_reason_and_info_source()
        self.validate_report_datetime_and_consent()
        self.validate_information_provider_is_alive()
        self._meta.model(**cleaned_data).has_previous_visit_or_raise(forms.ValidationError)
        return cleaned_data

    def validate_report_datetime_and_consent(self):
        cleaned_data = self.cleaned_data
        try:
            relative_identifier = cleaned_data.get('appointment').registered_subject.relative_identifier
            maternal_consent = MaternalConsent.objects.get(
                registered_subject__subject_identifier=relative_identifier)
            if cleaned_data.get("report_datetime") < maternal_consent.consent_datetime:
                raise forms.ValidationError("Report datetime CANNOT be before consent datetime")
            if cleaned_data.get("report_datetime").date() < maternal_consent.dob:
                raise forms.ValidationError("Report datetime CANNOT be before DOB")
        except MaternalConsent.DoesNotExist:
            raise forms.ValidationError('Maternal consent does not exist.')

    def validate_presence(self):
        cleaned_data = self.cleaned_data
        if cleaned_data.get('is_present') == YES:
            if cleaned_data.get('survival_status') == UNKNOWN:
                raise forms.ValidationError('Survival status cannot be unknown if infant is present')
            if cleaned_data.get('reason') in [MISSED_VISIT, LOST_VISIT, DEATH_VISIT]:
                raise forms.ValidationError(
                    'You indicated that infant visit reason is {}. You therefore CANNOT state that the infant is '
                    'present'.format(cleaned_data.get('reason')))

    def validate_reason_death(self):
        cleaned_data = self.cleaned_data
        if cleaned_data.get('reason') == DEATH_VISIT:
            if cleaned_data.get('survival_status') != DEAD:
                raise forms.ValidationError("A death is being reported. Select \'Deceased\' for survival status.")
            if cleaned_data.get('study_status') != OFF_STUDY:
                raise forms.ValidationError(
                    "This is an Off Study visit. Select \'off study\' for the infant's current study status.")

    def validate_reason_lost_and_completed(self):
        cleaned_data = self.cleaned_data
        if cleaned_data.get('reason') in [LOST_VISIT, OFF_STUDY]:
            if cleaned_data.get('study_status') != OFF_STUDY:
                raise forms.ValidationError(
                    "This is an Off Study or LFU visit. "
                    "Select \'off study\' for the infant's current study status.")

    def validate_reason_visit_missed(self):
        cleaned_data = self.cleaned_data
        if cleaned_data.get('reason') == MISSED_VISIT:
            if not cleaned_data.get('reason_missed'):
                raise forms.ValidationError("Provide reason scheduled visit was missed.")

    def validate_reason_and_info_source(self):
        cleaned_data = self.cleaned_data
        if cleaned_data.get('reason') != MISSED_VISIT:
            if not cleaned_data.get('info_source'):
                raise forms.ValidationError("Provide source of information.")

    def validate_survival_status_if_alive(self):
        cleaned_data = self.cleaned_data
        if cleaned_data.get('survival_status') in [ALIVE, DEAD]:
            if not cleaned_data.get('last_alive_date'):
                raise forms.ValidationError("Provide date infant last known alive.")

    def validate_information_provider_is_alive(self):
        cleaned_data = self.cleaned_data
        try:
            if cleaned_data.get('information_provider') == 'MOTHER':
                MaternalDeathReport.objects.get(
                    maternal_visit__appointment__registered_subject__subject_identifier=cleaned_data.get(
                        'appointment').registered_subject.relative_identifier)
                raise forms.ValidationError(
                    'The mother is indicated to be dead (MaternalDeathReport is filled). You '
                    'therefore CANNOT indicate the information provider for this infant to be '
                    'the mother')
        except MaternalDeathReport.DoesNotExist:
            pass

    class Meta:
        model = InfantVisit
        fields = '__all__'