from dateutil.relativedelta import relativedelta
from django.db import models
from django.utils import timezone
from django.conf import settings

from edc.subject.registration.models import RegisteredSubject
from edc_base.model.fields import IdentityTypeField
from edc.core.identifier.classes import SubjectIdentifier
from edc_base.model.fields.custom_fields import OmangField
from edc_base.model.models.base_uuid_model import BaseUuidModel
from edc_consent.models.base_consent import BaseConsent
from edc_consent.models.fields import (PersonalFieldsMixin, CitizenFieldsMixin,
                                       VulnerabilityFieldsMixin, IdentityFieldsMixin)
from edc_constants.choices import YES_NO_UNKNOWN, NO


class MaternalConsent(BaseConsent, IdentityFieldsMixin, PersonalFieldsMixin,
                      CitizenFieldsMixin, VulnerabilityFieldsMixin, BaseUuidModel):

    registered_subject = models.ForeignKey(RegisteredSubject, null=True)

    def __unicode__(self):
        return '{0} {1} {2} ({3})'.format(self.subject_identifier, self.first_name,
                                          self.last_name, self.initials)

    def save(self, *args, **kwargs):
        self.subject_identifier = SubjectIdentifier(site_code=settings.SITE_CODE).get_identifier()
        super(MaternalConsent, self).save(*args, **kwargs)

    class Meta:
        app_label = 'microbiome_maternal'
        verbose_name = 'Maternal Consent'
        verbose_name_plural = 'Maternal Consent'
