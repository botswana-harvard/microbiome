from django.db import models
from datetime import datetime

from edc.entry_meta_data.managers import EntryMetaDataManager
from edc.subject.off_study.models import BaseOffStudy
from edc_base.audit_trail import AuditTrail
from edc_base.model.models.base_uuid_model import BaseUuidModel

from .infant_visit import InfantVisit


class InfantOffStudy(BaseOffStudy, BaseUuidModel):

    """ A model completed by the user when the infant is taken off study. """
    infant_visit = models.OneToOneField(InfantVisit)

    report_datetime = models.DateTimeField(
        verbose_name="Visit Date and Time",
        default=datetime.today()
    )

    entry_meta_data_manager = EntryMetaDataManager(InfantVisit)

    objects = models.Manager()

    history = AuditTrail()

    def get_visit(self):
        return self.infant_visit

    def get_visit_model_cls(self):
        return InfantVisit

    def get_subject_identifier(self):
        return self.infant_visit.appointment.registered_subject.subject_identifier

    class Meta:
        app_label = "microbiome_infant"
        verbose_name = "Infant Off-Study"
        verbose_name_plural = "Infant Off-Study"
