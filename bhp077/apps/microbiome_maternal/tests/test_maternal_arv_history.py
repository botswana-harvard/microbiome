from django.test import TestCase
from django.utils import timezone
from dateutil.relativedelta import relativedelta
from datetime import date, datetime

from edc.core.bhp_variables.tests.factories.study_site_factory import StudySiteFactory
from edc.lab.lab_profile.classes import site_lab_profiles
from edc.lab.lab_profile.exceptions import AlreadyRegistered as AlreadyRegisteredLabProfile
from edc.subject.appointment.models import Appointment
from edc.subject.lab_tracker.classes import site_lab_tracker
from edc.subject.rule_groups.classes import site_rule_groups
from edc_constants.choices import YES, NO
from edc_constants.constants import CONTINUOUS, STOPPED, RESTARTED

from bhp077.apps.microbiome.app_configuration.classes import MicrobiomeConfiguration
from bhp077.apps.microbiome_lab.lab_profiles import MaternalProfile
from bhp077.apps.microbiome_list.models import PriorArv
from bhp077.apps.microbiome_maternal.forms import (MaternalArvHistoryForm)

from ..visit_schedule import PostnatalEnrollmentVisitSchedule

from .factories import (PostnatalEnrollmentFactory, MaternalVisitFactory,
                        MaternalEligibilityFactory, MaternalConsentFactory)


class TestMaternalArvHistory(TestCase):
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
        self.study_site = StudySiteFactory(site_code='10', site_name='Gabs')
        self.maternal_eligibility = MaternalEligibilityFactory()
        self.maternal_consent = MaternalConsentFactory(
            registered_subject=self.maternal_eligibility.registered_subject,
            study_site=self.study_site)
        self.registered_subject = self.maternal_consent.registered_subject
        self.postnatal_enrollment = PostnatalEnrollmentFactory(
            registered_subject=self.registered_subject,
            will_breastfeed=YES
        )
        self.appointment = Appointment.objects.get(registered_subject=self.registered_subject,
                                                   visit_definition__code='1000M')
        self.maternal_visit = MaternalVisitFactory(appointment=self.appointment)
        self.prior_arv = PriorArv.objects.create(name='ATZ', short_name='ATZ', field_name='prior_arv')
        self.data = {
            'maternal_visit': self.maternal_visit.id,
            'report_datetime': timezone.now(),
            'haart_start_date': date.today() - relativedelta(weeks=7),
            'is_date_estimated': '-',
            'preg_on_haart': YES,
            'haart_changes': 0,
            'prior_preg': CONTINUOUS,
            'prior_arv': [self.prior_arv.id],
        }

    def test_arv_interrupt_1(self):
        """Assert that if was not still on ARV then 'interruption never restarted' is not a valid option."""

        self.data['prior_preg'] = STOPPED
        self.data['haart_start_date'] = date(2015, 04, 10)
        self.data['preg_on_haart'] = YES
        form = MaternalArvHistoryForm(data=self.data)
        errors = ''.join(form.errors.get('__all__'))
        self.assertIn("You indicated that the mother was still on triple ARV when "
                      "she got pregnant, yet you indicated that ARVs were interrupted "
                      "and never restarted.", errors)

    def test_arv_interrupt_2(self):
        """Assert that if was not on ARV then 'Had treatment
        interruption but restarted' is not a valid option."""
        self.data['preg_on_haart'] = NO
        self.data['prior_preg'] = RESTARTED
        form = MaternalArvHistoryForm(data=self.data)
        errors = ''.join(form.errors.get('__all__'))
        self.assertIn(
            'You indicated that the mother was NOT on triple ARV when she got pregnant. '
            'ARVs could not have been interrupted. Please correct.', errors)

    def test_arv_interrupt_3(self):
        """Assert that if was not still on ARV then 'Received continuous HAART from the time she started'
           is not a valid option."""
        self.data['preg_on_haart'] = NO
        self.data['prior_preg'] = CONTINUOUS
        form = MaternalArvHistoryForm(data=self.data)
        errors = ''.join(form.errors.get('__all__'))
        self.assertIn(
            'You indicated that the mother was NOT on triple ARV when she got pregnant. '
            'ARVs could not have been uninterrupted. Please correct.', errors)

    def test_arv_interrupt_4(self):
        """Assert that if was not still on ARV only valid answer is 'interrupted and never restarted'"""
        self.data['preg_on_haart'] = NO
        self.data['prior_preg'] = STOPPED
        form = MaternalArvHistoryForm(data=self.data)
        self.assertTrue(form.is_valid())

    def test_haart_start_date(self):
        """ARV start date should be seex weeks prior to today"""
        self.data['haart_start_date'] = timezone.now()
        form = MaternalArvHistoryForm(data=self.data)
        errors = ''.join(form.errors.get('__all__'))
        self.assertIn("ARV start date (question 3) must be six weeks prior to today's date or greater.", errors)

    def test_haart_start_date_2(self):
        """Start date of ARVs CANNOT be before DOB"""
        self.data['haart_start_date'] = date(1987, 10, 10)
        self.data['report_datetime'] = datetime.today()
        form = MaternalArvHistoryForm(data=self.data)
        errors = ''.join(form.errors.get('__all__'))
        self.assertIn("Date of triple ARVs first started CANNOT be before DOB.", errors)
