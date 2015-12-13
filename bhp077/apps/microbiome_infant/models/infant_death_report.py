from django.db import models

from edc.entry_meta_data.managers import EntryMetaDataManager
from edc.subject.registration.models import RegisteredSubject
from edc_base.audit_trail import AuditTrail
from edc_base.model.models import BaseUuidModel
from edc_death_report.models import DeathReportMixin, InfantDrugRelationshipMixin

from .infant_visit import InfantVisit


class InfantDeathReport (DeathReportMixin, InfantDrugRelationshipMixin, BaseUuidModel):

    """ A model completed by the user after an infant's death. """

    VISIT_MODEL = InfantVisit

    registered_subject = models.OneToOneField(RegisteredSubject)

    infant_visit = models.OneToOneField(InfantVisit)

    objects = models.Manager()

    entry_meta_data_manager = EntryMetaDataManager(InfantVisit)

    history = AuditTrail()

    def get_report_datetime(self):
        return self.report_datetime

    def get_subject_identifier(self):
        return self.infant_visit.appointment.registered_subject.subject_identifier

    class Meta:
        app_label = "microbiome_infant"
        verbose_name = "Infant Death Report"