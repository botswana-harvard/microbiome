from django.core.urlresolvers import reverse
from django.db import models

from edc_base.audit_trail import AuditTrail
from edc_base.model.models.base_uuid_model import BaseUuidModel

from bhp077.apps.microbiome.choices import FEEDING_CHOICES

from ..choices import INFANT_VACCINATIONS

from .infant_scheduled_visit_model import InfantScheduledVisitModel


class InfantBirthFeedVaccine(InfantScheduledVisitModel):

    """ A model completed by the user on the infant's feeding & vaccination/ immunization. """

    feeding_after_delivery = models.CharField(
        max_length=50,
        choices=FEEDING_CHOICES,
        verbose_name="How was the infant being fed immediately after delivery? ",
        help_text=" ...before discharge from maternity")

    comments = models.TextField(
        max_length=250,
        verbose_name="Comment if any additional pertinent information: ",
        blank=True,
        null=True)

    objects = models.Manager()

    history = AuditTrail()

    class Meta:
        app_label = "microbiome_infant"
        verbose_name = "Infant Birth Feeding & Vaccination"
        verbose_name_plural = "Infant Birth Feeding & Vaccination"


class InfantVaccines(BaseUuidModel):

    infant_birth_feed_vaccine = models.ForeignKey(InfantBirthFeedVaccine)

    vaccination = models.CharField(
        choices=INFANT_VACCINATIONS,
        verbose_name="Since delivery, did the child receive any of the following vaccinations",
        max_length=100,
        null=True,
        blank=True,
    )

    vaccine_date = models.DateField(
        verbose_name='Date Vaccine was given',
        null=True,
        blank=True,
    )

    objects = models.Manager()

    history = AuditTrail()

    def __unicode__(self):
        return unicode(self.get_visit())

    def get_visit(self):
        return self.infant_birth_feed_vaccine.get_visit()

    def get_report_datetime(self):
        return self.infant_birth_feed_vaccine.get_report_datetime()

    def get_subject_identifier(self):
        return self.infant_birth_feed_vaccine.get_subject_identifier()

    def get_absolute_url(self):
        return reverse('admin:microbiome_infant_infantvaccines_change', args=(self.id,))

    class Meta:
        app_label = "microbiome_infant"
        verbose_name = "Infant Vaccines"
        verbose_name_plural = "Infant Vaccines"
