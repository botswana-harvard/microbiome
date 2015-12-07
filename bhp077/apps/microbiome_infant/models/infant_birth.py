from django.db import models

from edc.subject.appointment_helper.models import BaseAppointmentMixin
from edc.subject.registration.models import RegisteredSubject
from edc_base.audit_trail import AuditTrail
from edc_base.model.models import BaseUuidModel
from edc_base.model.validators import datetime_not_before_study_start, datetime_not_future
from edc_base.model.validators.date import date_not_future
from edc_constants.choices import GENDER_UNDETERMINED

from bhp077.apps.microbiome_maternal.models import MaternalLabourDel
from bhp077.apps.microbiome_infant.models.infant_off_study_mixin import InfantOffStudyMixin


class InfantBirth(InfantOffStudyMixin, BaseAppointmentMixin, BaseUuidModel):
    """ A model completed by the user on the infant's birth. """

    registered_subject = models.OneToOneField(RegisteredSubject, null=True)

    maternal_labour_del = models.ForeignKey(
        MaternalLabourDel,
        verbose_name="Mother's delivery record")

    report_datetime = models.DateTimeField(
        verbose_name="Date and Time infant enrolled",
        validators=[
            datetime_not_before_study_start,
            datetime_not_future, ],
        help_text='')

    first_name = models.CharField(
        max_length=25,
        verbose_name="Infant's first name",
        help_text="If infant name is unknown or not yet determined, "
                  "use Baby + birth order + mother's last name, e.g. 'Baby1Malane'")
    initials = models.CharField(
        max_length=2)

    dob = models.DateField(
        verbose_name='Date of Birth',
        help_text="Must match labour and delivery report.",
        validators=[date_not_future, ])

    gender = models.CharField(
        max_length=10,
        choices=GENDER_UNDETERMINED)

    objects = models.Manager()

    history = AuditTrail()

    def __unicode__(self):
        return "{} ({}) {}".format(self.first_name, self.initials, self.gender)

    def prepare_appointments(self, using):
        """To calculate infant appointments from date-of-delivery"""
        from edc.subject.appointment_helper.classes import AppointmentHelper
        if 'registered_subject' in dir(self):
            registered_subject = self.registered_subject
        else:
            registered_subject = RegisteredSubject.objects.get(subject_identifier=self.subject_identifier)
        relative_identifier = self.registered_subject.relative_identifier
        delivery = MaternalLabourDel.objects.filter(
            maternal_visit__appointment__registered_subject__subject_identifier=relative_identifier)
        if delivery:
            AppointmentHelper().create_all(
                registered_subject, self.__class__.__name__.lower(),
                using=using, source='BaseAppointmentMixin',
                base_appt_datetime=delivery[0].delivery_datetime)

    class Meta:
        app_label = "microbiome_infant"
        verbose_name = "Infant Birth Record"
        verbose_name_plural = "Infant Birth Record"
