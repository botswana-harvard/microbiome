from django.db import models

from edc_base.model.fields import OtherCharField
from edc_base.audit_trail import AuditTrail
from edc_constants.choices import YES_NO
from edc.subject.code_lists.models import WcsDxAdult

from .maternal_scheduled_visit_model import MaternalScheduledVisitModel
from microbiome.apps.mb_list.models import ChronicConditions
from .maternal_consent import MaternalConsent


class MaternalMedicalHistory(MaternalScheduledVisitModel):

    """ A model completed by the user on Medical History for all mothers. """

    CONSENT_MODEL = MaternalConsent

    chronic_cond_since = models.CharField(
        max_length=25,
        choices=YES_NO,
        verbose_name=("Does the mother have any significant chronic condition(s) that were"
                      " diagnosed prior to the current pregnancy and that remain ongoing?"),)

    chronic_cond = models.ManyToManyField(
        ChronicConditions,
        verbose_name="Chronic Diagnosis. Tick all that apply",
        help_text="")

    chronic_cond_other = OtherCharField(
        max_length=35,
        verbose_name="if other specify...",
        blank=True,
        null=True)

    who_diagnosis = models.CharField(
        max_length=25,
        choices=YES_NO,
        verbose_name=("Prior to the current pregnancy, was the participant ever diagnosed with"
                      " a WHO Stage III or IV illness?"),
        help_text="Please use the WHO Staging Guidelines. ONLY for HIV infected mothers")

    wcs_dx_adult = models.ManyToManyField(
        WcsDxAdult,
        verbose_name="List any new WHO Stage III/IV diagnoses that are not reported")

    history = AuditTrail()

    class Meta:
        app_label = 'mb_maternal'
        verbose_name = "Maternal Medical History"
        verbose_name_plural = "Maternal Medical History"