from django.db import models
from dateutil import rrule

from edc_base.model.validators import date_not_before_study_start, date_not_future

from edc_constants.choices import (POS_NEG_UNTESTED_REFUSAL, YES_NO_NA, POS_NEG, YES, YES_NO, NO)
from edc_constants.constants import NOT_APPLICABLE

from .maternal_eligibility import MaternalEligibility


class EnrollmentMixin(models.Model):

    """Base Model for antenal and postnatal enrollment"""

    is_diabetic = models.CharField(
        verbose_name='Are you diabetic?',
        default=NO,
        choices=YES_NO,
        help_text='INELIGIBLE if YES',
        max_length=3)

    on_tb_treatment = models.CharField(
        verbose_name="Are you being treated for tubercolosis?",
        choices=YES_NO,
        default=NO,
        help_text='INELIGIBLE if YES',
        max_length=3)

    on_hypertension_treatment = models.CharField(
        verbose_name='Are you being treated for hypertension?',
        choices=YES_NO,
        default=NO,
        help_text='INELIGIBLE if YES',
        max_length=3
    )

    breastfeed_for_a_year = models.CharField(
        verbose_name='Are you willing to breast-feed your child for a whole year?',
        choices=YES_NO,
        default=NO,
        help_text='INELIGIBLE if NO',
        max_length=3)

    instudy_for_a_year = models.CharField(
        verbose_name="Are you willing to remain in the study during the infants first year of life",
        choices=YES_NO,
        default=NO,
        help_text='INELIGIBLE if NO',
        max_length=3)

    week32_test = models.CharField(
        verbose_name="Have you tested for HIV on OR after 32 weeks gestational age?",
        choices=YES_NO,
        default=NO,
        max_length=3)

    date_of_test = models.DateField(
        verbose_name="Date of HIV Test",
        null=True,
        blank=True)

    week32_result = models.CharField(
        verbose_name="What was your result?",
        choices=POS_NEG,
        max_length=15,
        null=True,
        blank=True)

    verbal_hiv_status = models.CharField(
        verbose_name="What is your current HIV status?",
        choices=POS_NEG_UNTESTED_REFUSAL,
        max_length=30,
        help_text=("if POS or NEG, ask for documentation."))

    evidence_hiv_status = models.CharField(
        verbose_name="(Interviewer) Have you seen evidence of the HIV result?",
        max_length=15,
        null=True,
        blank=False,
        default=NOT_APPLICABLE,
        choices=YES_NO_NA,
        help_text=("evidence = clinic and/or IDCC records. check regimes/drugs. If NO, participant"
                   "will not be enrolled"))

    valid_regimen = models.CharField(
        verbose_name="(Interviewer) If HIV +VE, do records show that participant takes ARV'\s?",
        choices=YES_NO_NA,
        null=True,
        blank=False,
        default=NOT_APPLICABLE,
        max_length=15,
        help_text=("Valid regimes include: Atripla, Truvada-Efavirenz or Tenofovir, "
                   "Entricitibine-Efavirenz, Truvad-Lamivudine-Efavirenz. If NO, participant"
                   "will not be enrolled"))

    valid_regimen_duration = models.CharField(
        verbose_name="Has the participant been on the regimen for a valid period of time?",
        choices=YES_NO_NA,
        null=True,
        blank=False,
        default=NOT_APPLICABLE,
        max_length=15,
        help_text=("If not 6 or more weeks then not eligible."))

    process_rapid_test = models.CharField(
        verbose_name="Was a rapid test processed?",
        choices=YES_NO_NA,
        null=True,
        blank=False,
        default=NOT_APPLICABLE,
        max_length=15,
        help_text=(
            'Remember, rapid test is for HIV -VE, UNTESTED, UNKNOWN, REFUSED-to-ANSWER verbal responses'))

    date_of_rapid_test = models.DateField(
        verbose_name="Date of rapid test",
        null=True,
        validators=[
            date_not_before_study_start,
            date_not_future, ],
        blank=True)

    rapid_test_result = models.CharField(
        verbose_name="What is the rapid test result?",
        choices=POS_NEG,
        max_length=15,
        null=True,
        blank=True)

    def get_registration_datetime(self):
        return self.report_datetime

    @property
    def requires_rapid_test(self):
        weeks_since_test = rrule.rrule(
            rrule.WEEKLY, dtstart=self.date_of_test, until=self.report_datetime.date()).count()
        value = self.weeks_base - weeks_since_test
        return value >= 32

    def maternal_eligibility_pregnant_yes(self):
        try:
            return MaternalEligibility.objects.get(
                registered_subject__subject_identifier=self.get_subject_identifier(),
                currently_pregnant=YES,
            )
        except MaternalEligibility.DoesNotExist:
            return False
        return True

    def maternal_eligibility_pregnant_currently_delivered_yes(self):
        try:
            return MaternalEligibility.objects.get(
                registered_subject__subject_identifier=self.get_subject_identifier(),
                recently_delivered=YES,
            )
        except MaternalEligibility.DoesNotExist:
            return False
        return True

    def get_subject_identifier(self):
        return self.registered_subject.subject_identifier

    def __unicode__(self):
        return "{0} {1}".format(
            self.registered_subject.subject_identifier,
            self.registered_subject.first_name)

    class Meta:
        abstract = True
