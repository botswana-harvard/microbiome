from django.core.urlresolvers import reverse
from django.db import models

from .base_enrollment import BaseEnrollment


class AntenatalEnrollment(BaseEnrollment):

    weeks_of_gestation = models.IntegerField(
        verbose_name="How many weeks pregnant?",
        null=True,
        blank=True,
        help_text="IF >=32 weeks do rapid test", )

    def get_absolute_url(self):
        return reverse('admin:microbiome_antenatalenrollment_change', args=(self.id,))

    class Meta:
        app_label = 'microbiome'
        verbose_name = 'Antenatal Enrollment'
        verbose_name_plural = 'Antenatal Enrollment'