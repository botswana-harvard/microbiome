from django.db import models

from datetime import datetime

from edc_base.model.models.base_uuid_model import BaseUuidModel
from edc_base.audit_trail import AuditTrail
from edc.entry_meta_data.managers import EntryMetaDataManager
from edc.data_manager.models import TimePointStatusMixin

from .infant_visit import InfantVisit
from .infant_off_study_mixin import InfantOffStudyMixin


class InfantScheduledVisitModel(InfantOffStudyMixin, BaseUuidModel,
                                TimePointStatusMixin):

    """ A model completed by the user on the infant's scheduled visit. """

    infant_visit = models.OneToOneField(InfantVisit)

    report_datetime = models.DateTimeField(
        verbose_name="Visit Date and Time",
        default=datetime.today()
    )

    entry_meta_data_manager = EntryMetaDataManager(InfantVisit)

    objects = models.Manager()

    history = AuditTrail()

    def get_consenting_subject_identifier(self):
        """Returns mother's identifier."""
        return self.get_visit().appointment.registered_subject.relative_identifier

    def get_subject_identifier(self):
        return self.get_visit().appointment.registered_subject.subject_identifier

    def get_report_datetime(self):
        return self.report_datetime

    def get_visit(self):
        return self.infant_visit

    class Meta:
        abstract = True
