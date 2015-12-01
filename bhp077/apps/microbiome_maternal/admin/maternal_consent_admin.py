from django.contrib import admin

from edc_base.modeladmin.admin import BaseModelAdmin
from edc.subject.registration.models import RegisteredSubject
from edc_consent.actions import flag_as_verified_against_paper, unflag_as_verified_against_paper

from bhp077.apps.microbiome_maternal.forms import MaternalConsentForm
from bhp077.apps.microbiome_maternal.models import MaternalConsent


class MaternalConsentAdmin(BaseModelAdmin):

    form = MaternalConsentForm

    fields = ('registered_subject',
              'first_name',
              'last_name',
              'initials',
              'language',
              'study_site',
              'recruit_source',
              'recruit_source_other',
              'recruitment_clinic',
              'recruitment_clinic_other',
              'is_literate',
              'witness_name',
              'consent_datetime',
              'dob',
              'is_dob_estimated',
              'citizen',
              'identity',
              'identity_type',
              'confirm_identity',
              'comment',
              'consent_reviewed',
              'study_questions',
              'assessment_score',
              'consent_signature',
              'consent_copy')
    actions = [flag_as_verified_against_paper, unflag_as_verified_against_paper]
    radio_fields = {'citizen': admin.VERTICAL,
                    'study_site': admin.VERTICAL,
                    'language': admin.VERTICAL,
                    'study_site': admin.VERTICAL,
                    'recruit_source': admin.VERTICAL,
                    'recruitment_clinic': admin.VERTICAL,
                    'is_literate': admin.VERTICAL,
                    'is_dob_estimated': admin.VERTICAL,
                    'identity_type': admin.VERTICAL,
                    'consent_reviewed': admin.VERTICAL,
                    'study_questions': admin.VERTICAL,
                    'assessment_score': admin.VERTICAL,
                    'consent_signature': admin.VERTICAL,
                    'consent_copy': admin.VERTICAL}
    list_display = ('subject_identifier',
                    'registered_subject',
                    'is_verified',
                    'is_verified_datetime',
                    'first_name',
                    'initials',
                    'gender',
                    'dob',
                    'consent_datetime',
                    'recruit_source',
                    'recruitment_clinic',
                    'created',
                    'modified',
                    'user_created',
                    'user_modified')
    list_filter = ('language',
                   'is_verified',
                   'is_literate',
                   'identity_type')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "registered_subject":
            if request.GET.get('registered_subject'):
                kwargs["queryset"] = RegisteredSubject.objects.filter(
                    id__exact=request.GET.get('registered_subject', 0))
            else:
                self.readonly_fields = list(self.readonly_fields)
                try:
                    self.readonly_fields.index('registered_subject')
                except ValueError:
                    self.readonly_fields.append('registered_subject')
        return super(MaternalConsentAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(MaternalConsent, MaternalConsentAdmin)
