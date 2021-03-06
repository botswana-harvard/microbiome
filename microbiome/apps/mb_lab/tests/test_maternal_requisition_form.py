from django.utils import timezone

from edc_appointment.models import Appointment
from edc_constants.choices import YES, NO, POS

from microbiome.apps.mb_lab.models.aliquot import AliquotType
from microbiome.apps.mb_maternal.tests.factories import (
    PostnatalEnrollmentFactory, MaternalVisitFactory)
from microbiome.apps.mb_maternal.tests.factories import MaternalEligibilityFactory
from microbiome.apps.mb_maternal.tests.factories import MaternalConsentFactory

from ..forms import MaternalRequisitionForm
from ..models import Panel

from edc_constants.constants import SCHEDULED, UNSCHEDULED

from .base_test_case import BaseTestCase


class TestMaternalRequisitionForm(BaseTestCase):
    """Test eligibility of a mother for postnatal followup."""

    def setUp(self):
        super(TestMaternalRequisitionForm, self).setUp()
        self.maternal_eligibility = MaternalEligibilityFactory()
        self.maternal_consent = MaternalConsentFactory(
            registered_subject=self.maternal_eligibility.registered_subject,
            study_site=self.study_site)
        self.registered_subject = self.maternal_consent.registered_subject
        postnatal_enrollment = PostnatalEnrollmentFactory(
            current_hiv_status=POS,
            evidence_hiv_status=YES,
            registered_subject=self.registered_subject,
            will_breastfeed=YES)
        self.assertTrue(postnatal_enrollment.is_eligible)
        appointment = Appointment.objects.get(
            registered_subject=self.registered_subject,
            visit_definition__code='1000M')
        MaternalVisitFactory(appointment=appointment, reason=SCHEDULED)
        self.appointment = Appointment.objects.get(
            registered_subject=self.registered_subject,
            visit_definition__code='2000M')
        self.panel = Panel.objects.get(name='Breast Milk (Storage)')
        self.aliquot_type = AliquotType.objects.get(alpha_code='WB')
        self.data = {
            'maternal_visit': None,
            'requisition_identifier': 'ZXDF39U',
            'requisition_datetime': timezone.now(),
            'report_datetime': timezone.now(),
            'is_drawn': NO,
            'reason_not_drawn': 'collection_failed',
            'drawn_datetime': '',
            'study_site': self.study_site,
            'panel': self.panel.id,
            'aliquot_type': self.aliquot_type.id,
            'item_type': 'tube',
            'item_count_total': '',
            'estimated_volume': '',
            'priority': '',
            'comments': '',
        }

    def test_visit_reason_unscheduled(self):
        maternal_visit = MaternalVisitFactory(
            appointment=self.appointment, reason=UNSCHEDULED)
        self.data['maternal_visit'] = maternal_visit.id
        self.data['is_drawn'] = YES
        self.data['drawn_datetime'] = timezone.now() - timezone.timedelta(hours=1)
        self.data['item_count_total'] = 1
        self.data['estimated_volume'] = 5.0
        self.data['reason_not_drawn'] = None
        self.data['priority'] = 'normal'
        form = MaternalRequisitionForm(data=self.data)
        self.assertTrue(form.is_valid())
