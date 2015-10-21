from django.core.urlresolvers import reverse
from django.db import models

from edc.lab.lab_requisition.models import BaseRequisition
from edc_base.audit_trail import AuditTrail
from edc_base.model.models.base_uuid_model import BaseUuidModel

from microbiome.maternal.models import MaternalVisit

from .aliquot_type import AliquotType
from .packing_list import PackingList
from .panel import Panel

from .managers import RequisitionManager


class MaternalRequisition(BaseRequisition, BaseUuidModel):

    maternal_visit = models.ForeignKey(MaternalVisit)

    entry_meta_data_manager = RequisitionManager(MaternalVisit)

    packing_list = models.ForeignKey(PackingList, null=True, blank=True)

    aliquot_type = models.ForeignKey(AliquotType)

    panel = models.ForeignKey(Panel)

    history = AuditTrail()

    def get_visit(self):
        return self.maternal_visit

    def aliquot(self):
        url = reverse('admin:microbiome_lab_aliquot_changelist')
        return """<a href="{url}?q={requisition_identifier}" />aliquot</a>""".format(url=url, requisition_identifier=self.requisition_identifier)
    aliquot.allow_tags = True

    class Meta:
        app_label = 'microbiome_lab'
        verbose_name = 'Maternal Requisition'
        unique_together = ('maternal_visit', 'panel', 'is_drawn')
        ordering = ('-created', )