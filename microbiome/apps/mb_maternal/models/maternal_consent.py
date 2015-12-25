from django.db import models
from django.conf import settings

from edc.core.bhp_variables.models import StudySite
from edc.core.bhp_variables.utils import default_study_site
from edc.core.identifier.classes import SubjectIdentifier
from edc.subject.registration.models import RegisteredSubject
from edc_base.audit_trail import AuditTrail
from edc_base.model.fields import OtherCharField
from edc.device.sync.models import BaseSyncUuidModel
from edc_consent.models.base_consent import BaseConsent
from edc_consent.models.fields import (
    PersonalFieldsMixin, CitizenFieldsMixin, ReviewFieldsMixin, VulnerabilityFieldsMixin)
from edc_consent.models.fields.bw import IdentityFieldsMixin
from edc_offstudy.models import OffStudyMixin

from microbiome.apps.mb.constants import MIN_AGE_OF_CONSENT, MAX_AGE_OF_CONSENT

from ..maternal_choices import RECRUIT_SOURCE, RECRUIT_CLINIC


class MaternalConsent(BaseConsent, OffStudyMixin, ReviewFieldsMixin,
                      IdentityFieldsMixin, PersonalFieldsMixin,
                      CitizenFieldsMixin, VulnerabilityFieldsMixin, BaseSyncUuidModel):

    """ A model completed by the user on the mother's consent. """

    MIN_AGE_OF_CONSENT = MIN_AGE_OF_CONSENT
    MAX_AGE_OF_CONSENT = MAX_AGE_OF_CONSENT

    off_study_model = ('mb_maternal', 'MaternalOffStudy')

    registered_subject = models.OneToOneField(RegisteredSubject, null=True)

    study_site = models.ForeignKey(StudySite, default=lambda: default_study_site('site_code', settings.SITE_CODE))

    recruit_source = models.CharField(
        max_length=75,
        choices=RECRUIT_SOURCE,
        verbose_name="The mother first learned about the Microbiome study from ")

    recruit_source_other = OtherCharField(
        max_length=35,
        verbose_name="if other recruitment source, specify...",
        blank=True,
        null=True)

    recruitment_clinic = models.CharField(
        max_length=100,
        verbose_name="The mother was recruited from",
        choices=RECRUIT_CLINIC)

    recruitment_clinic_other = models.CharField(
        max_length=100,
        verbose_name="if other recruitment clinic, specify...",
        blank=True,
        null=True, )

    history = AuditTrail()

    def __unicode__(self):
        return '{0} {1} {2} ({3})'.format(self.subject_identifier, self.first_name,
                                          self.last_name, self.initials)

    def save(self, *args, **kwargs):
        self.subject_identifier = SubjectIdentifier(site_code=self.study_site.site_code).get_identifier()
        self.gender = self.maternal_eligibility.registered_subject.gender
        super(MaternalConsent, self).save(*args, **kwargs)

    def get_registration_datetime(self):
        return self.consent_datetime

    def get_subject_identifier(self):
        return self.subject_identifier

    @property
    def maternal_eligibility(self):
        from ..models import MaternalEligibility
        try:
            maternal_eligibility = MaternalEligibility.objects.get(registered_subject=self.registered_subject)
            return maternal_eligibility
        except MaternalEligibility.DoesNotExist:
            return None

    class Meta:
        app_label = 'mb_maternal'
        verbose_name = 'Maternal Consent'
        verbose_name_plural = 'Maternal Consent'
