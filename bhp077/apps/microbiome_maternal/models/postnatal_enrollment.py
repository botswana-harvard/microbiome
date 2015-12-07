from django.db import models
from django.db.models import get_model

from edc.subject.appointment_helper.models import BaseAppointmentMixin
from edc.subject.registration.models import RegisteredSubject
from edc_base.audit_trail import AuditTrail
from edc_base.model.models import BaseUuidModel
from edc_base.model.validators import (datetime_not_before_study_start, datetime_not_future,)
from edc_consent.models import RequiresConsentMixin
from edc_constants.choices import YES_NO, YES, NO, POS, NEG

from ..maternal_choices import LIVE_STILL_BIRTH, LIVE

from .enrollment_mixin import EnrollmentMixin
from .maternal_consent import MaternalConsent
from .maternal_off_study_mixin import MaternalOffStudyMixin
from edc_constants.constants import NEVER, UNKNOWN, DWTA


class PostnatalEnrollment(EnrollmentMixin, MaternalOffStudyMixin, BaseAppointmentMixin,
                          RequiresConsentMixin, BaseUuidModel):

    CONSENT_MODEL = MaternalConsent

    weeks_base_field = 'gestation_wks_delivered'  # for rapid test required calc

    registered_subject = models.OneToOneField(RegisteredSubject, null=True)

    report_datetime = models.DateTimeField(
        verbose_name="Date and Time of  Postnatal Enrollment",
        validators=[
            datetime_not_before_study_start,
            datetime_not_future, ],
        help_text='')

    postpartum_days = models.IntegerField(
        verbose_name="How many days postpartum?",
        help_text="If more than 3days, not eligible")

    vaginal_delivery = models.CharField(
        verbose_name="Was this a vaginal delivery?",
        choices=YES_NO,
        max_length=3,
        help_text="INELIGIBLE if NO")

    gestation_wks_delivered = models.IntegerField(
        verbose_name="How many weeks after gestation was the child born?",
        help_text="ineligible if premature or born before 37weeks")

    delivery_status = models.CharField(
        verbose_name="Was this a live or still birth?",
        choices=LIVE_STILL_BIRTH,
        max_length=15,
        help_text='if still birth, not eligible')

    is_eligible = models.BooleanField(
        editable=False)

    live_infants = models.IntegerField(
        verbose_name="How many live infants?",
        null=True,
        blank=True)

    objects = models.Manager()

    history = AuditTrail()

    def save(self, *args, **kwargs):
        self.is_eligible = self.check_eligiblity()
        super(PostnatalEnrollment, self).save(*args, **kwargs)

    def get_registration_datetime(self):
        return self.report_datetime

    def check_eligiblity(self):
        """Returns true if the participant is eligible."""
        eligible = False
        if (self.delivery_status == LIVE and
                self.gestation_wks_delivered >= 37 and
                self.is_diabetic == NO and
                self.on_hypertension_tx == NO and
                self.on_tb_tx == NO and
                self.postpartum_days <= 3 and
                self.vaginal_delivery == YES and
                self.will_breastfeed == YES and
                self.will_remain_onstudy == YES):
            if (self.current_hiv_status == POS and
                    self.evidence_hiv_status == YES and
                    self.valid_regimen == YES and
                    self.valid_regimen_duration == YES):
                eligible = True
            elif (self.current_hiv_status == POS and
                    self.evidence_hiv_status == NO and
                    self.rapid_test_result == POS and
                    self.valid_regimen == YES and
                    self.valid_regimen_duration == YES):
                eligible = True
            elif (self.current_hiv_status == NEG and
                  self.evidence_hiv_status == NO and
                  self.rapid_test_result == NEG):
                eligible = True
            elif (self.current_hiv_status == NEG and
                  self.evidence_hiv_status == YES):
                eligible = True
            elif (self.current_hiv_status in [NEVER, UNKNOWN, DWTA] and
                    self.rapid_test_result == NEG):
                eligible = True
        return eligible

    @property
    def antenatal_enrollment(self):
        AntenatalEnrollment = get_model('microbiome_maternal', 'antenatalenrollment')
        try:
            return AntenatalEnrollment.objects.get(registered_subject=self.registered_subject)
        except AntenatalEnrollment.DoesNotExist:
            return None
        return None

    class Meta:
        app_label = 'microbiome_maternal'
        verbose_name = 'Postnatal Enrollment'
        verbose_name_plural = 'Postnatal Enrollment'
