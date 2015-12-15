from django.db import models

from edc_base.audit_trail import AuditTrail
from edc_base.model.fields.custom_fields import OtherCharField
from edc_base.model.validators import date_not_future
from edc_consent.plain_fields import IsDateEstimatedField
from edc_constants.choices import YES_NO, YES_NO_NA, YES_NO_UNSURE_NA
from edc_constants.constants import NOT_APPLICABLE

from microbiome.apps.mb.choices import COWS_MILK, TIMES_BREASTFED, WATER_USED

from .infant_scheduled_visit_model import InfantScheduledVisitModel


class InfantFeeding(InfantScheduledVisitModel):

    """ A model completed by the user on the infant's feeding. """

    last_att_sche_visit = models.DateField(
        verbose_name=("When was the last attended scheduled visit where an infant feeding form"
                      " was completed? "),
        help_text="",
        blank=True,
        null=True)

    other_feeding = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name=("Since the last attended scheduled visit where an infant feeding form"
                      " was completed, has the participant received any formula milk or other"
                      " foods or liquids other than breast-milk? "),
        help_text="If Formula Feeding or received any other foods or liquids answer YES.")

    formula_intro_occur = models.CharField(
        max_length=3,
        choices=YES_NO_NA,
        verbose_name=("Did the introduction of formula or other foods or liquids to the"
                      " participant occur before the last attended scheduled visit where"
                      " an infant feeding form was completed?"),
        help_text=(""),
        default=NOT_APPLICABLE)

    formula_intro_date = models.DateField(
        verbose_name=("Date participant first received formula milk (or other foods or liquids)"
                      "since last attended scheduled visit where an infant feeding form"
                      " was completed"),
        help_text="",
        blank=True,
        null=True)

    took_formula = models.CharField(
        max_length=10,
        choices=YES_NO_UNSURE_NA,
        verbose_name="Since the last attended scheduled visit where an infant feeding form was completed "
                     "did the participant take Formula?",
        help_text="If formula feeding since last visit answer YES",
        default=NOT_APPLICABLE)

    is_first_formula = models.CharField(
        verbose_name="Is this the first reporting of infant formula use?",
        max_length=15,
        choices=YES_NO,
        blank=True,
        null=True,)

    date_first_formula = models.DateField(
        verbose_name="Date infant formula introduced?",
        validators=[date_not_future, ],
        blank=True,
        null=True,
        help_text="provide date if this is first reporting of infant formula")

    est_date_first_formula = IsDateEstimatedField(
        verbose_name="Is date infant formula introduced estimated?",
        blank=True,
        null=True,
        help_text="provide date if this is first reporting of infant formula")

    water = models.CharField(
        max_length=10,
        choices=YES_NO_UNSURE_NA,
        verbose_name="Since the last attended scheduled visit where an infant feeding form was completed did "
                     "the participant take Water?",
        help_text="Not as part of formula milk",
        default=NOT_APPLICABLE)

    juice = models.CharField(
        max_length=10,
        choices=YES_NO_UNSURE_NA,
        verbose_name="Since the last attended scheduled visit where an infant feeding form was completed "
                     "did the participant take Juice?",
        help_text="If you answered YES to Q3 you must answer YES, NO or NOT SURE to this question, "
                  "you may not answer N/A ",
        default=NOT_APPLICABLE)

    cow_milk = models.CharField(
        max_length=15,
        choices=YES_NO_UNSURE_NA,
        verbose_name="Since the last attended scheduled visit where an infant feeding form was completed "
                     "did the participant take Cow's milk?",
        help_text="",
        default=NOT_APPLICABLE)

    cow_milk_yes = models.CharField(
        verbose_name="If 'Yes', cow's milk was...",
        max_length=25,
        choices=COWS_MILK,
        help_text="",
        default='N/A')

    other_milk = models.CharField(
        max_length=15,
        choices=YES_NO_UNSURE_NA,
        verbose_name="Since the last attended scheduled visit where an infant feeding form was "
                     "completed did the participant take Other animal milk?",
        help_text="",
        default=NOT_APPLICABLE)

    other_milk_animal = OtherCharField(
        max_length=35,
        verbose_name="If 'Yes' specify which animal:",
        help_text="",
        blank=True,
        null=True)

    milk_boiled = models.CharField(
        max_length=10,
        choices=YES_NO_UNSURE_NA,
        verbose_name="Was milk boiled?",
        help_text="",
        default=NOT_APPLICABLE)

    fruits_veg = models.CharField(
        max_length=10,
        choices=YES_NO_UNSURE_NA,
        verbose_name="Since the last attended scheduled visit where an infant feeding form was completed "
                     "did the participant take Fruits/vegetables",
        help_text="",
        default=NOT_APPLICABLE)

    cereal_porridge = models.CharField(
        max_length=12,
        choices=YES_NO_UNSURE_NA,
        verbose_name="Since the last attended scheduled visit where an infant feeding form was completed "
                     "did the participant take Cereal/porridge?",
        help_text="",
        default=NOT_APPLICABLE)

    solid_liquid = models.CharField(
        max_length=10,
        choices=YES_NO_UNSURE_NA,
        verbose_name="Since the last attended scheduled visit where an infant feeding form was "
                     "completed did the participant take Other solids and liquids",
        help_text="",
        default=NOT_APPLICABLE)

    rehydration_salts = models.CharField(
        max_length=3,
        choices=YES_NO_UNSURE_NA,
        verbose_name="Since the last attended scheduled visit where an infant feeding form was completed "
                     "did the participant take Oral rehydaration salts",
        help_text="",
        default=NOT_APPLICABLE)

    water_used = models.CharField(
        max_length=50,
        verbose_name="What water do you usually use to prepare the participant's milk?",
        choices=WATER_USED,
        help_text="",
        default=NOT_APPLICABLE)

    water_used_other = OtherCharField(
        max_length=35,
        verbose_name="If 'other', specify",
        blank=True,
        null=True)

    ever_breastfeed = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name="Since the last attended scheduled visit,did the infant ever breast-feed",
        help_text="")

    complete_weaning = models.CharField(
        max_length=3,
        choices=YES_NO_NA,
        verbose_name="If 'NO', did complete weaning from breast milk take place before the last "
                     "attended scheduled visit?",
        help_text="",
        default=NOT_APPLICABLE)

    weaned_completely = models.CharField(
        max_length=3,
        choices=YES_NO_NA,
        verbose_name=("Is the participant currently completely weaned from breast milk"
                      " (at least 72 hours without breast feeding,no intention to re-start)?"),
        help_text="",
        default=NOT_APPLICABLE)

    most_recent_bm = models.DateField(
        verbose_name="Date of most recent breastfeeding ",
        help_text="",
        blank=True,
        null=True)

    times_breastfed = models.CharField(
        max_length=50,
        verbose_name=("Between the last attended scheduled visit where an infant feeding form"
                      " was completed and date of most recent breastfeeding,how often did"
                      " the participant receive breast milk for feeding?"),
        choices=TIMES_BREASTFED,
        help_text="",
        default=NOT_APPLICABLE)

    comments = models.TextField(
        max_length=200,
        verbose_name="List any comments about participant's feeding that are not answered above",
        blank=True,
        null=True)

    history = AuditTrail()

    def save(self, *args, **kwargs):
        if self.previous_infant_feeding:
            self.last_att_sche_visit = self.previous_infant_feeding
        super(InfantFeeding, self).save(*args, **kwargs)

    def previous_infant_instance(self, infant_visit):
        """ Returns previous infant visit. """
        from .infant_visit import InfantVisit
        from edc.subject.appointment.models import Appointment
        visit = ['2000', '2010', '2030', '2060', '2090', '2120']
        try:
            registered_subject = infant_visit.appointment.registered_subject
            previous_visit_code = visit[visit.index(self.infant_visit.appointment.visit_definition.code) - 1]
            previous_appointment = Appointment.objects.get(registered_subject=registered_subject,
                                                           visit_definition__code=previous_visit_code)
            return InfantVisit.objects.get(appointment=previous_appointment)
        except Appointment.DoesNotExist:
            return None
        except InfantVisit.DoesNotExist:
            return None
        except AttributeError:
            return None

    @property
    def previous_infant_feeding(self):
        """ Return previous infant feeding from. """
        visit = ['2000', '2010', '2030', '2060', '2090', '2120']

        if (
            not self.infant_visit.appointment.visit_definition.code == '2000' and
            not self.infant_visit.appointment.visit_definition.code == '2010'
        ):
            prev_visit_index = visit.index(self.infant_visit.appointment.visit_definition.code) - 1
            while prev_visit_index > 0:
                try:
                    return InfantFeeding.objects.get(
                        infant_visit__appointment__visit_definition__code=visit[prev_visit_index]
                    ).report_datetime.date()
                except InfantFeeding.DoesNotExist:
                    prev_visit_index = prev_visit_index - 1
        return None

    class Meta:
        app_label = "mb_infant
"
        verbose_name = "Infant Feeding"
        verbose_name_plural = "Infant Feeding"