from django.test import TestCase

from edc.core.bhp_variables.tests.factories.study_site_factory import StudySiteFactory
from edc.lab.lab_profile.classes import site_lab_profiles
from edc.lab.lab_profile.exceptions import AlreadyRegistered as AlreadyRegisteredLabProfile
from edc.subject.appointment.models import Appointment
from edc.subject.lab_tracker.classes import site_lab_tracker
from edc.subject.rule_groups.classes import site_rule_groups
from edc_constants.choices import YES

from microbiome.apps.mb.app_configuration.classes import MicrobiomeConfiguration
from microbiome.apps.mb_lab.lab_profiles import MaternalProfile
from microbiome.apps.mb_lab.models.aliquot import AliquotType
from microbiome.apps.mb_maternal.visit_schedule import PostnatalEnrollmentVisitSchedule
from microbiome.apps.mb_maternal.tests.factories import (PostnatalEnrollmentFactory, MaternalVisitFactory)
from microbiome.apps.mb_maternal.tests.factories import MaternalEligibilityFactory
from microbiome.apps.mb_maternal.tests.factories import MaternalConsentFactory

from ..models import Panel

from .factories import MaternalRequistionFactory
from edc_constants.constants import UNSCHEDULED, SCHEDULED, POS


class TestMaternalRequisitionModel(TestCase):
    """Test eligibility of a mother for postnatal followup."""

    def setUp(self):
        try:
            site_lab_profiles.register(MaternalProfile())
        except AlreadyRegisteredLabProfile:
            pass
        MicrobiomeConfiguration().prepare()
        site_lab_tracker.autodiscover()
        PostnatalEnrollmentVisitSchedule().build()
        site_rule_groups.autodiscover()
        self.study_site = StudySiteFactory(site_code=10, site_name='Gabs')
        self.maternal_eligibility = MaternalEligibilityFactory()
        self.maternal_consent = MaternalConsentFactory(
            registered_subject=self.maternal_eligibility.registered_subject,
            study_site=self.study_site)
        self.registered_subject = self.maternal_consent.registered_subject
        self.postnatal_enrollment = PostnatalEnrollmentFactory(
            current_hiv_status=POS,
            evidence_hiv_status=YES,
            registered_subject=self.registered_subject,
            will_breastfeed=YES)
        appointment = Appointment.objects.get(
            registered_subject=self.registered_subject,
            visit_definition__code='1000M')
        MaternalVisitFactory(appointment=appointment, reason=SCHEDULED)
        self.appointment = Appointment.objects.get(
            registered_subject=self.registered_subject,
            visit_definition__code='2000M')
        self.panel = Panel.objects.get(name='Breast Milk (Storage)')
        self.aliquot_type = AliquotType.objects.get(alpha_code='WB')

    def test_visit_reason_scheduled(self):
        maternal_visit = MaternalVisitFactory(appointment=self.appointment, reason=SCHEDULED)
        MaternalRequistionFactory(
            maternal_visit=maternal_visit,
            panel=self.panel,
            study_site=self.study_site,
            aliquot_type=self.aliquot_type)

    def test_visit_reason_unscheduled(self):
        maternal_visit = MaternalVisitFactory(appointment=self.appointment, reason=UNSCHEDULED)
        MaternalRequistionFactory(
            maternal_visit=maternal_visit,
            panel=self.panel,
            study_site=self.study_site,
            aliquot_type=self.aliquot_type)
