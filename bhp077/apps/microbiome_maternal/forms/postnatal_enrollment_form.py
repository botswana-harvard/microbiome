from django import forms

from edc_constants.constants import POS, YES

from .base_enrollment_form import BaseEnrollmentForm
from bhp077.apps.microbiome.constants import LIVE
from bhp077.apps.microbiome_maternal.models import PostnatalEnrollment, AntenatalEnrollment


class PostnatalEnrollmentForm(BaseEnrollmentForm):

    def clean(self):

        cleaned_data = super(PostnatalEnrollmentForm, self).clean()
        if cleaned_data.get('gestation_before_birth') > 45:
            raise forms.ValidationError('Gestational age of {} exceeds 45 weeks. Please correct.'
                                        .format(cleaned_data.get('gestation_before_birth')))
        if cleaned_data.get("live_or_still_birth") == LIVE:
            if not cleaned_data.get('live_infants'):
                raise forms.ValidationError("Live infants were born. How many?")
            if cleaned_data.get('live_infants', None) <= 0:
                raise forms.ValidationError("Live infants were born. Number cannot be zero or less")
        try:
            ant = AntenatalEnrollment.objects.get(
                registered_subject__subject_identifier=cleaned_data.get('registered_subject').subject_identifier)
        except AntenatalEnrollment.DoesNotExist:
            ant = None
        if ant:
            if ant.verbal_hiv_status == POS and ant.evidence_hiv_status == YES:
                if not cleaned_data.get('verbal_hiv_status') == POS or not cleaned_data.get('evidence_hiv_status') == YES:
                    raise forms.ValidationError("Antenatal Enrollment shows participant is {} and {} evidence ."
                                                " Please Correct {} and {} evidence".format(ant.verbal_hiv_status,
                                                                                            ant.evidence_hiv_status,
                                                                                            cleaned_data.get('verbal_hiv_status'),
                                                                                            cleaned_data.get('evidence_hiv_status')))
        if ant:
            if not ant.antenatal_eligible:
                raise forms.ValidationError("This mother is not eligible for postnatal enrollment. Failed antenatal enrollment.")

        return cleaned_data

    class Meta:
        model = PostnatalEnrollment
        fields = '__all__'
