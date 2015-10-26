from django.core.urlresolvers import reverse
from django.db import models

from edc_constants.choices import YES_NO, YES_NO_NA

from .base_mother import BaseMother
from microbiome.maternal.maternal_choices import KNOW_HIV_STATUS


class MaternalInfected(BaseMother):

    prior_health_haart = models.CharField(
        max_length=25,
        choices=YES_NO,
        verbose_name="Before this pregnancy, was the mother on HAART for her own health",
        help_text=("For her own health and not just PMTCT for an earlier pregnancy or "
                   "breastfeeding.",))
    prev_pregnancy_arv = models.CharField(
        max_length=25,
        choices=YES_NO_NA,
        verbose_name="Was the mother on any ARVs during previous pregnancies (or immediately following delivery) "
                     "for PMTCT purposes (and not for her own health)? ",
        help_text="not including this pregnancy", )

    know_hiv_status = models.CharField(
        max_length=50,
        verbose_name="How many people know that you are HIV infected?",
        choices=KNOW_HIV_STATUS,
        help_text="",)

    def get_absolute_url(self):
        return reverse('admin:maternal_maternalinfected_change', args=(self.id,))

    class Meta:
        app_label = 'maternal'
        verbose_name = 'Maternal Infected'
        verbose_name_plural = 'Maternal Infected'
