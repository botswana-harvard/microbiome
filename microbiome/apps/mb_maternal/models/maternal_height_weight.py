from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from edc_base.audit_trail import AuditTrail

from .maternal_crf_model import MaternalCrfModel


class MaternalHeightWeight(MaternalCrfModel):

    """ A model completed by the user on Height, Weight details for all mothers. """

    weight_kg = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="Mother's weight? ",
        validators=[MinValueValidator(30), MaxValueValidator(136), ],
        help_text="Measured in Kilograms (kg)")
    height = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="Mother's height? ",
        validators=[MinValueValidator(134), MaxValueValidator(195), ],
        help_text="Measured in Centimeters (cm)")

    systolic_bp = models.IntegerField(
        max_length=3,
        verbose_name="Mother's systolic blood pressure?",
        validators=[MinValueValidator(75), MaxValueValidator(220), ],
        help_text="in mm e.g. 120, should be between 75 and 220."
    )

    diastolic_bp = models.IntegerField(
        max_length=3,
        verbose_name="Mother's diastolic blood pressure?",
        validators=[MinValueValidator(35), MaxValueValidator(130), ],
        help_text="in hg e.g. 80, should be between 35 and 130.")

    history = AuditTrail()

    class Meta:
        app_label = 'mb_maternal'
        verbose_name = 'Maternal Height & Weight'
        verbose_name_plural = 'Maternal Height & Weight'
