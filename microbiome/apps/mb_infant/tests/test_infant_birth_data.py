from django import forms
from django.utils import timezone

from edc_appointment.models import Appointment
from edc_registration.models import RegisteredSubject
from edc_constants.constants import YES, NO, NEG

from microbiome.apps.mb.constants import INFANT
from microbiome.apps.mb_infant.forms import InfantBirthDataForm
from microbiome.apps.mb_infant.models import InfantBirthData
from microbiome.apps.mb_infant.tests.factories import InfantBirthFactory, InfantVisitFactory
from microbiome.apps.mb_maternal.tests.factories import MaternalConsentFactory, MaternalLabourDelFactory
from microbiome.apps.mb_maternal.tests.factories import MaternalEligibilityFactory, MaternalVisitFactory
from microbiome.apps.mb_maternal.tests.factories import PostnatalEnrollmentFactory

from .base_test_case import BaseTestCase


class BaseTestInfantBirthDataModel(InfantBirthData):
    class Meta:
        app_label = 'mb_infant'


class BaseTestInfantBirthDataForm(InfantBirthDataForm):

    class Meta:
        model = BaseTestInfantBirthDataModel
        fields = '__all__'


class TestInfantBirthData(BaseTestCase):

    def setUp(self):
        super(TestInfantBirthData, self).setUp()

        self.maternal_eligibility = MaternalEligibilityFactory()
        self.maternal_consent = MaternalConsentFactory(
            registered_subject=self.maternal_eligibility.registered_subject)
        self.registered_subject = self.maternal_eligibility.registered_subject
        PostnatalEnrollmentFactory(
            registered_subject=self.registered_subject,
            current_hiv_status=NEG,
            evidence_hiv_status=YES,
            rapid_test_done=YES,
            rapid_test_result=NEG)
        self.appointment = Appointment.objects.get(
            registered_subject=self.registered_subject,
            visit_definition__code='1000M')
        self.maternal_visit = MaternalVisitFactory(appointment=self.appointment)
        self.appointment = Appointment.objects.get(
            registered_subject=self.registered_subject,
            visit_definition__code='2000M')
        maternal_visit = MaternalVisitFactory(appointment=self.appointment)
        maternal_labour_del = MaternalLabourDelFactory(maternal_visit=maternal_visit)
        infant_registered_subject = RegisteredSubject.objects.get(
            relative_identifier=self.registered_subject.subject_identifier,
            subject_type=INFANT)
        self.infant_birth = InfantBirthFactory(
            registered_subject=infant_registered_subject,
            maternal_labour_del=maternal_labour_del)
        self.appointment = Appointment.objects.get(
            registered_subject=infant_registered_subject,
            visit_definition__code='2000')
        self.infant_visit = InfantVisitFactory(appointment=self.appointment)
        self.data = {
            'report_datetime': timezone.now(),
            'infant_birth': self.infant_birth.id,
            'infant_visit': self.infant_visit.id,
            'weight_kg': 3.61,
            'infant_length': 89.97,
            'head_circumference': 39.30,
            'apgar_score': NO,
            'apgar_score_min_1': '',
            'apgar_score_min_5': '',
            'apgar_score_min_10': '',
            'congenital_anomalities': NO}

    def test_infant_length(self):
        self.data['infant_birth'] = self.infant_visit.id
        self.data['infant_length'] = 95.62
        self.assertRaises(forms.ValidationError)

    def test_validate_infant_head_cir(self):
        self.data['infant_birth'] = self.infant_visit.id
        self.data['head_circumference'] = 41.23
        self.assertRaises(forms.ValidationError)

    def test_validate_apgar_1(self):
        self.data['apgar_score'] = YES
        form = InfantBirthDataForm(data=self.data)
        errors = ''.join(form.errors.get('__all__'))
        self.assertIn('If Apgar scored performed, then you should answer At 1 minute', errors)

    def test_validate_apgar_2(self):
        self.data['apgar_score'] = YES
        form = InfantBirthDataForm(data=self.data)
        errors = ''.join(form.errors.get('__all__'))
        self.assertIn('If Apgar scored performed, then you should answer At 1 minute', errors)

    def test_validate_apgar_3(self):
        self.data['apgar_score'] = YES
        self.data['apgar_score_min_1'] = 3
        form = InfantBirthDataForm(data=self.data)
        errors = ''.join(form.errors.get('__all__'))
        self.assertIn('If Apgar scored performed, then you should answer At 5 minute', errors)

    def test_validate_apgar_4(self):
        self.data['apgar_score'] = NO
        self.data['apgar_score_min_1'] = 3
        form = InfantBirthDataForm(data=self.data)
        errors = ''.join(form.errors.get('__all__'))
        self.assertIn('If Apgar scored was NOT performed, then you should NOT answer at 1 minute', errors)

    def test_validate_apgar_5(self):
        self.data['apgar_score'] = NO
        self.data['apgar_score_min_5'] = 3
        form = InfantBirthDataForm(data=self.data)
        errors = ''.join(form.errors.get('__all__'))
        self.assertIn('If Apgar scored was NOT performed, then you should NOT answer at 5 minute', errors)

    def test_validate_apgar_6(self):
        self.data['apgar_score'] = NO
        self.data['apgar_score_min_10'] = 3
        form = InfantBirthDataForm(data=self.data)
        errors = ''.join(form.errors.get('__all__'))
        self.assertIn('If Apgar scored was NOT performed, then you should NOT answer at 10 minute', errors)
