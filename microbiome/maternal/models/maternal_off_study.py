from django.db import models
from django.core.urlresolvers import reverse

from edc.entry_meta_data.managers import EntryMetaDataManager
from edc.subject.off_study.models import BaseOffStudy
from edc_base.audit_trail import AuditTrail

from .maternal_visit import MaternalVisit


class MaternalOffStudy(BaseOffStudy):

    """A model completed by the user that completed when the subject is taken off-study."""

    history = AuditTrail()

    maternal_visit = models.OneToOneField(MaternalVisit)

    entry_meta_data_manager = EntryMetaDataManager(MaternalVisit)

    def get_visit(self):
        return self.maternal_visit

    def get_absolute_url(self):
        return reverse('admin:maternal_maternaloffstudy_change', args=(self.id,))

    class Meta:
        app_label = 'maternal'
        verbose_name = "Maternal Off Study"
        verbose_name_plural = "Maternal Off Study"
