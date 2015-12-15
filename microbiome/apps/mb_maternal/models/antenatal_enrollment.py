from django.db import models

from edc.subject.appointment_helper.models import BaseAppointmentMixin
from edc.subject.registration.models import RegisteredSubject
from edc_base.audit_trail import AuditTrail
from edc_base.model.models import BaseUuidModel
from edc_base.model.validators import (datetime_not_before_study_start, datetime_not_future,)
from edc_consent.models import RequiresConsentMixin

from .enrollment_mixin import EnrollmentMixin
from .maternal_consent import MaternalConsent
from .maternal_off_study_mixin import MaternalOffStudyMixin
from .postnatal_enrollment import PostnatalEnrollment
from ..managers import AntenatalEnrollmentManager


class AntenatalEnrollment(EnrollmentMixin, MaternalOffStudyMixin, BaseAppointmentMixin,
                          RequiresConsentMixin, BaseUuidModel):

    CONSENT_MODEL = MaternalConsent

    weeks_base_field = 'gestation_wks'  # for rapid test required calc

    registered_subject = models.OneToOneField(RegisteredSubject, null=True)

    report_datetime = models.DateTimeField(
        verbose_name="Report date",
        validators=[
            datetime_not_before_study_start,
            datetime_not_future, ],
        help_text='')

    gestation_wks = models.IntegerField(
        verbose_name="How many weeks pregnant?",
        help_text=" (weeks of gestation). Eligible if >=36 weeks", )

    objects = AntenatalEnrollmentManager()

    history = AuditTrail()

    def natural_key(self):
        return (self.report_datetime, self.registered_subject.natural_key())

    def save(self, *args, **kwargs):
        self.update_common_fields_to_postnatal_enrollment()
        super(AntenatalEnrollment, self).save(*args, **kwargs)

    def update_common_fields_to_postnatal_enrollment(self):
        """Updates common field values from Antenatal Enrollment to
        Postnatal Enrollment if Postnatal Enrollment exists.

        Confirms is_eligible does not change value before saving."""
        if self.id and self.is_eligible:
            try:
                postnatal_enrollment = PostnatalEnrollment.objects.get(
                    registered_subject=self.registered_subject)
                is_eligible = postnatal_enrollment.is_eligible
                for attrname in self.common_fields():
                    setattr(postnatal_enrollment, attrname, getattr(self, attrname))
                if postnatal_enrollment.check_eligiblity() != is_eligible:
                    raise ValueError(
                        'Eligiblity calculated for Postnatal Enrollment unexpectedly '
                        'changed after updating values from Antenatal Enrollment. '
                        'Got \'is_eligible\' changed from {} to {}.'.format(
                            is_eligible, postnatal_enrollment.is_eligible))
                else:
                    postnatal_enrollment.save()
            except PostnatalEnrollment.DoesNotExist:
                pass

    class Meta:
        app_label = 'mb_maternal'
        verbose_name = 'Antenatal Enrollment'
        verbose_name_plural = 'Antenatal Enrollment'