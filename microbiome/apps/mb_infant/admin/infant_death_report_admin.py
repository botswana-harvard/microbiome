from collections import OrderedDict

from django.contrib import admin

from edc_export.actions import export_as_csv_action
from edc_base.modeladmin.admin import BaseModelAdmin
from edc_registration.models import RegisteredSubject

from ..forms import InfantDeathReportForm
from ..models import InfantDeathReport, InfantVisit


class InfantDeathReportAdmin(BaseModelAdmin):

    form = InfantDeathReportForm

    fields = (
        "infant_visit",
        "registered_subject",
        "report_datetime",
        "death_date",
        "cause",
        "cause_other",
        "perform_autopsy",
        "death_cause",
        "cause_category",
        "cause_category_other",
        "diagnosis_code",
        "diagnosis_code_other",
        "illness_duration",
        "medical_responsibility",
        "participant_hospitalized",
        "reason_hospitalized",
        "reason_hospitalized_other",
        "days_hospitalized",
        "study_drug_relationship",
        "infant_nvp_relationship",
        "haart_relationship",
        "trad_med_relationship",
        "comment",
    )

    radio_fields = {
        "reason_hospitalized": admin.VERTICAL,
        "medical_responsibility": admin.VERTICAL,
        "cause": admin.VERTICAL,
        "cause_category": admin.VERTICAL,
        "perform_autopsy": admin.VERTICAL,
        "participant_hospitalized": admin.VERTICAL,
        "study_drug_relationship": admin.VERTICAL,
        "infant_nvp_relationship": admin.VERTICAL,
        "haart_relationship": admin.VERTICAL,
        "trad_med_relationship": admin.VERTICAL,
        "diagnosis_code": admin.VERTICAL
    }

    actions = [
        export_as_csv_action(
            description="CSV Export of Infant Death",
            fields=[],
            delimiter=',',
            exclude=['created', 'modified', 'user_created', 'user_modified', 'revision', 'id', 'hostname_created',
                     'hostname_modified'],
            extra_fields=OrderedDict(
                {'subject_identifier': 'registered_subject__subject_identifier',
                 'gender': 'registered_subject__gender',
                 'dob': 'registered_subject__dob',
                 }),
        )]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "infant_visit":
            if request.GET.get('infant_visit'):
                kwargs["queryset"] = InfantVisit.objects.filter(id=request.GET.get('infant_visit'))
        if db_field.name == "registered_subject":
            if request.GET.get('infant_visit'):
                infant_visit = InfantVisit.objects.get(id=request.GET.get('infant_visit'))
                kwargs["queryset"] = RegisteredSubject.objects.filter(
                    subject_identifier=infant_visit.appointment.registered_subject.subject_identifier)
        return super(InfantDeathReportAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(InfantDeathReport, InfantDeathReportAdmin)
