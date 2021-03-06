from django.db import models

from edc_base.audit_trail import AuditTrail
from edc_constants.choices import YES_NO, YES_NO_NA
from edc_constants.constants import NOT_APPLICABLE

from microbiome.apps.mb.choices import BREAST_CHOICE

from .maternal_crf_model import MaternalCrfModel


class MaternalBreastHealth(MaternalCrfModel):

    """ A model completed by the user on the mother's General post-partum follow-up. """

    breast_feeding = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name="Is the mother currently breastfeeding?",
    )

    has_mastitis = models.CharField(
        max_length=15,
        choices=YES_NO_NA,
        verbose_name="Is there evidence of mastitis?",
        default=NOT_APPLICABLE,
    )

    mastitis = models.CharField(
        max_length=20,
        choices=BREAST_CHOICE,
        verbose_name="Where is mastitis evident?",
        default=NOT_APPLICABLE,
    )

    has_lesions = models.CharField(
        max_length=15,
        choices=YES_NO_NA,
        verbose_name="Are there any lesions such as ulcers, vesicles or sores on the breasts?",
        default=NOT_APPLICABLE,
    )

    lesions = models.CharField(
        max_length=20,
        choices=BREAST_CHOICE,
        verbose_name="Where are the lesions evident?",
        default=NOT_APPLICABLE,
    )

    advised_stop_bf = models.CharField(
        max_length=15,
        choices=YES_NO_NA,
        verbose_name="Was the mother advised to discontinue breastfeeding?",
        default=NOT_APPLICABLE,
    )

    why_not_advised = models.CharField(
        max_length=100,
        verbose_name="Please provide a reason why breastfeeding cessation was not advised?",
        blank=True,
        null=True,
    )

    history = AuditTrail()

    class Meta:
        app_label = 'mb_maternal'
        verbose_name = "Maternal Breast Health"
        verbose_name_plural = "Maternal Breast Health"
