from django.db import models
from django.core.urlresolvers import reverse

from .infant_arv_proph import InfantArvProph
from .infant_scheduled_visit_model import InfantScheduledVisitModel


class InfantArvProphMod(InfantScheduledVisitModel):

    infant_arv_proph = models.ForeignKey(InfantArvProph)

    other_reason = models.CharField(
        verbose_name="Specify Other",
        max_length=100,
        null=True,
        blank=True,
    )

    def __str__(self):
        return str(self.infant_arv_proph.infant_visit)

    def get_absolute_url(self):
        return reverse('admin:microbiome_infant_infantarvprophmod_change', args=(self.id,))

    class Meta:
        app_label = "microbiome_infant"
        verbose_name = 'Infant NVP or AZT Proph: Mods'