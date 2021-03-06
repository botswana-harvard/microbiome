from datetime import date
from django.utils import timezone

from edc_appointment.models import Appointment
from edc_registration.models import RegisteredSubject
from edc_constants.constants import YES, NO, NEG
from edc_death_report.models.reason_hospitalized import ReasonHospitalized

from microbiome.apps.mb.constants import INFANT
from microbiome.apps.mb_infant.forms import InfantDeathReportForm
from microbiome.apps.mb_infant.tests.factories import InfantBirthFactory, InfantVisitFactory
from microbiome.apps.mb_maternal.tests.factories import (
    MaternalConsentFactory, MaternalLabourDelFactory)
from microbiome.apps.mb_maternal.tests.factories import (
    MaternalEligibilityFactory, MaternalVisitFactory)
from microbiome.apps.mb_maternal.tests.factories import PostnatalEnrollmentFactory

from .base_test_case import BaseTestCase


class TestInfantDeathReportForm(BaseTestCase):

    def setUp(self):
        super(TestInfantDeathReportForm, self).setUp()
        maternal_eligibility = MaternalEligibilityFactory(
            report_datetime=timezone.now())
        maternal_consent = MaternalConsentFactory(
            registered_subject=maternal_eligibility.registered_subject)
        registered_subject = maternal_consent.registered_subject
        maternal_subject_identifier = maternal_consent.subject_identifier

        postnatal_enrollment = PostnatalEnrollmentFactory(
            registered_subject=registered_subject,
            current_hiv_status=NEG,
            evidence_hiv_status=YES,
            rapid_test_done=YES,
            rapid_test_date=date.today(),
            rapid_test_result=NEG)
        self.assertTrue(postnatal_enrollment.is_eligible)
        appointment1 = Appointment.objects.get(
            registered_subject=registered_subject,
            visit_definition__code='1000M')
        MaternalVisitFactory(appointment=appointment1)
        appointment = Appointment.objects.get(
            registered_subject=postnatal_enrollment.registered_subject,
            visit_definition__code='2000M')
        maternal_visit = MaternalVisitFactory(appointment=appointment)
        maternal_labour_del = MaternalLabourDelFactory(maternal_visit=maternal_visit)

        infant_registered_subject = RegisteredSubject.objects.get(
            subject_type=INFANT,
            relative_identifier=maternal_subject_identifier)
        InfantBirthFactory(
            registered_subject=infant_registered_subject,
            maternal_labour_del=maternal_labour_del)
        appointment2000 = Appointment.objects.get(
            registered_subject=infant_registered_subject,
            visit_definition__code='2000')
        InfantVisitFactory(appointment=appointment2000)
        appointment2010 = Appointment.objects.get(
            registered_subject=infant_registered_subject,
            visit_definition__code='2010')
        infant_visit = InfantVisitFactory(appointment=appointment2010)

        # requery
        infant_registered_subject = RegisteredSubject.objects.get(pk=infant_registered_subject.pk)

        self.data = {
            'registered_subject': infant_registered_subject.id,
            'report_datetime': timezone.now(),
            'infant_visit': infant_visit.id,
            'death_date': timezone.now().date(),
            'death_cause_info': 'N/A',
            'death_cause_info_other': NO,
            'perform_autopsy': NO,
            'death_cause': NO,
            'death_cause_category': NO,
            'death_cause_other': None,
            'illness_duration': None,
            'death_medical_responsibility': None,
            'participant_hospitalized': YES,
            'reason_hospitalized': None,
            'days_hospitalized': 0,
            'study_drug_relate': None,
            'infant_nvp_relate': None,
            'haart_relate': None,
            'trad_med_relate': None,
            'comment': None,
        }

    def test_hospitalized_no_reason(self):
        """Test participant hospitalized and no reason for hospitalization"""
        self.data['participant_hospitalized'] = YES
        self.data['reason_hospitalized'] = None
        infant_death_form = InfantDeathReportForm(data=self.data)
        self.assertIn(
            'If the participant was hospitalized, indicate '
            'the primary reason.',
            infant_death_form.errors.get('__all__'))

    def test_hospitalized_reason_given_no_days(self):
        """Test participant hospitalized and reason given but number of days hospitalized not
            given"""
        self.data['participant_hospitalized'] = YES
        reason_hospitalized = ReasonHospitalized.objects.get(name='Sepsis (unspecified)')
        self.data['reason_hospitalized'] = reason_hospitalized.id
        self.data['days_hospitalized'] = 0
        infant_death_form = InfantDeathReportForm(data=self.data)
        self.assertIn(
            'If the participant was hospitalized, indicate '
            'for how many days.',
            infant_death_form.errors.get('__all__'))

    def test_not_hospitalized_but_reason_given(self):
        """Test participant not hospitalized but hospilization reason given"""
        self.data['participant_hospitalized'] = NO
        reason_hospitalized = ReasonHospitalized.objects.get(name='Sepsis (unspecified)')
        self.data['reason_hospitalized'] = reason_hospitalized.id
        infant_death_form = InfantDeathReportForm(data=self.data)
        self.assertIn(
            'If the participant was not hospitalized, do not indicate the primary reason.',
            infant_death_form.errors.get('__all__'))

    def test_not_hospitalized_but_no_days_given(self):
        """Test participant not hospitalized but days hospitalization given"""
        self.data['participant_hospitalized'] = NO
        self.data['reason_hospitalized'] = None
        self.data['days_hospitalized'] = 10
        infant_death_form = InfantDeathReportForm(data=self.data)
        self.assertIn(
            'If the participant was not hospitalized, do not indicate for how many days.',
            infant_death_form.errors.get('__all__'))
