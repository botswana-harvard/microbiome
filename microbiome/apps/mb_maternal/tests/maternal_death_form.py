from django.test import TestCase
from django.utils import timezone

from edc.lab.lab_profile.classes import site_lab_profiles
from edc.subject.lab_tracker.classes import site_lab_tracker
from edc.subject.rule_groups.classes import site_rule_groups
from edc.lab.lab_profile.exceptions import AlreadyRegistered as AlreadyRegisteredLabProfile
from edc.subject.appointment.models import Appointment
from edc_constants.constants import YES, NO, NEG

from microbiome.apps.mb.app_configuration.classes import MicrobiomeConfiguration
from microbiome.apps.mb_maternal.forms import MaternalDeathReportForm

from microbiome.apps.mb_lab.lab_profiles import MaternalProfile
from microbiome.apps.mb_maternal.tests.factories import MaternalConsentFactory, MaternalLabourDelFactory
from microbiome.apps.mb_maternal.tests.factories import MaternalEligibilityFactory, MaternalVisitFactory
from microbiome.apps.mb_maternal.tests.factories import PostnatalEnrollmentFactory
from microbiome.apps.mb_maternal.visit_schedule import PostnatalEnrollmentVisitSchedule


class TestMaternalDeathReportForm(TestCase):

    def setUp(self):
        try:
            site_lab_profiles.register(MaternalProfile())
        except AlreadyRegisteredLabProfile:
            pass
        MicrobiomeConfiguration().prepare()
        site_lab_tracker.autodiscover()
        PostnatalEnrollmentVisitSchedule().build()
        site_rule_groups.autodiscover()

        self.maternal_eligibility = MaternalEligibilityFactory()
        self.maternal_consent = MaternalConsentFactory(registered_subject=self.maternal_eligibility.registered_subject)
        self.registered_subject = self.maternal_eligibility.registered_subject

        PostnatalEnrollmentFactory(
            registered_subject=self.registered_subject,
            current_hiv_status=NEG,
            evidence_hiv_status=YES,
            rapid_test_done=YES,
            rapid_test_result=NEG)
        self.appointment = Appointment.objects.get(
            registered_subject=self.registered_subject, visit_definition__code='1000M')
        self.maternal_visit = MaternalVisitFactory(appointment=self.appointment)
        self.appointment = Appointment.objects.get(
            registered_subject=self.registered_subject, visit_definition__code='2000M')
        self.maternal_visit = MaternalVisitFactory(appointment=self.appointment)
        MaternalLabourDelFactory(maternal_visit=self.maternal_visit)

        self.data = {
            'report_datetime': timezone.now(),
            'maternal_visit': self.maternal_visit.id,
            'death_date': timezone.now().date(),
            'death_cause_info': 'N/A',
            'death_cause_info_other': NO,
            'perform_autopsy': NO,
            'death_cause': NO,
            'death_cause_category': NO,
            'death_cause_other': None,
            'illness_duration': None,
            'death_medical_responsibility': None,
            'articipant_hospitalized': None,
            'death_reason_hospitalized': None,
            'participant_hospitalized': YES,
            'death_reason_hospitalized': None,
            'days_hospitalized': 0,
            'study_drug_relate': None,
            'maternal_nvp_relate': None,
            'haart_relate': None,
            'trad_med_relate': None,
            'comment': None,
        }

    def test_maternal_death_form_valid(self):
        maternal_death_form = MaternalDeathReportForm(data=self.data)
        self.assertTrue(maternal_death_form.is_valid())

    def test_maternal_validate_date_of_death(self):
        self.data['death_date'] = timezone.now().date()
        self.maternal_consent.consent_datetime = timezone.now()
        self.maternal_consent.save()
        maternal_death_form = MaternalDeathReportForm(data=self.data)
        self.assertIn(
            u'Consent_Datetime CANNOT be before consent datetime', maternal_death_form.errors.get('__all__'))

    def test_death_reason_hospitalized_yes(self):
        self.data['participant_hospitalized'] = YES
        self.data['death_reason_hospitalized"'] = None
        maternal_death_form = MaternalDeathReportForm(data=self.data)
        self.assertIn(
            u'If the participant was hospitalized, what was the primary reason for hospitalisation?',
            maternal_death_form.errors.get('__all__'))

    def test_death_reason_hospitalized_yes1(self):
        self.data['participant_hospitalized'] = YES
        self.data['death_reason_hospitalized"'] = None
        self.data['days_hospitalized'] = 0
        maternal_death_form = MaternalDeathReportForm(data=self.data)
        self.assertIn(
            u'If the participant was hospitalized, please provide number of days the participant was hospitalised.',
            maternal_death_form.errors.get('__all__'))