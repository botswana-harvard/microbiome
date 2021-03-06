from django.db import models
from django.core.validators import MinValueValidator

from edc_base.model.fields import IsDateEstimatedField, OtherCharField
from edc_base.audit_trail import AuditTrail
from edc_constants.choices import YES_NO

from microbiome.apps.mb_list.models import PriorArv

from ..maternal_choices import PRIOR_PREG_HAART_STATUS

from .maternal_crf_model import MaternalCrfModel


class MaternalArvHistory(MaternalCrfModel):

    """ A model completed by the user on ARV history for infected mothers only. """

    haart_start_date = models.DateField(
        verbose_name="Date of triple antiretrovirals first started")

    is_date_estimated = IsDateEstimatedField(
        verbose_name=("Is the subject's date of triple antiretrovirals estimated?"))

    preg_on_haart = models.CharField(
        max_length=25,
        choices=YES_NO,
        verbose_name=("Was she still on triple antiretrovirals at the time she became pregnant"
                      " for this pregnancy? "))

    haart_changes = models.IntegerField(
        validators=[MinValueValidator(0)],
        verbose_name="How many times did you change your triple antiretrovirals medicines?")

    prior_preg = models.CharField(
        max_length=80,
        verbose_name="Prior to this pregnancy the mother has ",
        choices=PRIOR_PREG_HAART_STATUS)

    prior_arv = models.ManyToManyField(
        PriorArv,
        verbose_name=("Please list all of the ARVs that the mother "
                      "ever received prior to the current pregnancy:"))

    prior_arv_other = OtherCharField(
        max_length=35,
        verbose_name="if other specify...",
        blank=True,
        null=True)

    history = AuditTrail()

    class Meta:
        app_label = 'mb_maternal'
        verbose_name = "Maternal ARV History"
        verbose_name_plural = "Maternal ARV History"
