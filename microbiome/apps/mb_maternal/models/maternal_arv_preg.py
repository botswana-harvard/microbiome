from django.db import models

from edc_base.audit_trail import AuditTrail
from edc_base.model.models.base_uuid_model import BaseUuidModel
from edc_constants.choices import YES_NO
from edc.subject.haart.choices import ARV_DRUG_LIST

from microbiome.apps.mb.choices import ARV_INTERRUPTION_REASON

from .maternal_scheduled_visit_model import MaternalScheduledVisitModel
from .maternal_consent import MaternalConsent
from ..managers import MaternalArvManager
from edc_constants.constants import NOT_APPLICABLE


class MaternalArvPreg(MaternalScheduledVisitModel):

    CONSENT_MODEL = MaternalConsent

    """ This model is for all HIV positive mothers who are pregnant (whom we hope to enroll their infant)
     and/or for mothers who have just delivered """

    took_arv = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name="Did the mother receive any ARVs during this pregnancy?",
        help_text="(NOT including single -dose NVP in labour)")

    is_interrupt = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name="Was there an interruption in the ARVs received during pregnancy through delivery of >/=3days?",
    )

    interrupt = models.CharField(
        verbose_name="Please give reason for interruption",
        max_length=50,
        choices=ARV_INTERRUPTION_REASON,
        default=NOT_APPLICABLE)

    interrupt_other = models.TextField(
        max_length=250,
        verbose_name="Other, specify ",
        blank=True,
        null=True)

    history = AuditTrail()

    class Meta:
        app_label = 'mb_maternal'
        verbose_name = 'Maternal ARV In This Preg: Pregnancy'
        verbose_name_plural = 'Maternal ARV In This Preg: Pregnancy'


class MaternalArv(BaseUuidModel):

    """ ARV table to indicate ARV medication taken by mother """

    maternal_arv_preg = models.ForeignKey(MaternalArvPreg)

    arv_code = models.CharField(
        verbose_name="ARV code",
        null=True,
        blank=True,
        max_length=35,
        choices=ARV_DRUG_LIST,)

    start_date = models.DateField(
        verbose_name="Date Started",
        null=True,
        blank=True)

    stop_date = models.DateField(
        verbose_name="Date Stopped",
        null=True,
        blank=True)

    objects = MaternalArvManager()

    history = AuditTrail()

    def natural_key(self):
        return (self.maternal_arv_preg.natural_key())

    class Meta:
        app_label = 'mb_maternal'
        verbose_name = 'Maternal ARV'
        verbose_name_plural = 'Maternal ARV'