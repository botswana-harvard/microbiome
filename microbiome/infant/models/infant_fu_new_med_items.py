from django.db import models
from django.core.urlresolvers import reverse

from edc_constants.choices import DRUG_ROUTE
from ..choices import MEDICATIONS

from infant.models.infant_fu_new_med import InfantFuNewMed


class InfantFuNewMedItems(models.Model):

    infant_fu_med = models.ForeignKey(InfantFuNewMed)

    medication = models.CharField(
        max_length=100,
        choices=MEDICATIONS,
        verbose_name="Medication",
        blank=True,
        null=True,
    )

    drug_route = models.CharField(
        max_length=20,
        choices=DRUG_ROUTE,
        verbose_name="Drug route",
        blank=True,
        null=True,
    )

    def __str__(self):
        return str(self.infant_fu_med.infant_visit)

    def get_absolute_url(self):
        return reverse('admin:microbiome_infantfunewmeditems_change', args=(self.id,))

    class Meta:
        app_label = "microbiome"
        verbose_name = "Infant FollowUp: New Med Items"
        verbose_name_plural = "Infant FollowUp: New Med Items"