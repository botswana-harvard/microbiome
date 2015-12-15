from collections import OrderedDict

from django.contrib import admin

from edc.export.actions import export_as_csv_action

from ..models import InfantArvProphMod, InfantArvProph

from .base_infant_scheduled_modeladmin import BaseInfantScheduleModelAdmin


class InfantArvProphAdmin(BaseInfantScheduleModelAdmin):

    radio_fields = {
        'prophylatic_nvp': admin.VERTICAL,
        'arv_status': admin.VERTICAL,
    }

    actions = [
        export_as_csv_action(
            description="CSV Export of Infant NVP or AZT Proph",
            fields=[],
            delimiter=',',
            exclude=['created', 'modified', 'user_created', 'user_modified', 'revision', 'id', 'hostname_created',
                     'hostname_modified'],
            extra_fields=OrderedDict(
                {'subject_identifier': 'infant_visit__appointment__registered_subject__subject_identifier',
                 'gender': 'infant_visit__appointment__registered_subject__gender',
                 'dob': 'infant_visit__appointment__registered_subject__dob',
                 }),
        )]
admin.site.register(InfantArvProph, InfantArvProphAdmin)


class InfantArvProphModAdmin(BaseInfantScheduleModelAdmin):

    list_filter = ('infant_arv_proph',)

    actions = [
        export_as_csv_action(
            description="CSV Export of Infant NVP or AZT Proph",
            fields=[],
            delimiter=',',
            exclude=['created', 'modified', 'user_created', 'user_modified', 'revision', 'id', 'hostname_created',
                     'hostname_modified'],
            extra_fields=OrderedDict(
                {'subject_identifier':
                 'infant_arv_proph__infant_visit__appointment__registered_subject__subject_identifier',
                 'gender': 'infant_arv_proph__infant_visit__appointment__registered_subject__gender',
                 'dob': 'infant_arv_proph__infant_visit__appointment__registered_subject__dob',
                 'prophylatic_nvp': 'infant_arv_proph__prophylatic_nvp',
                 'arv_status': 'infant_arv_proph__arv_status',
                 }),
        )]

admin.site.register(InfantArvProphMod, InfantArvProphModAdmin)