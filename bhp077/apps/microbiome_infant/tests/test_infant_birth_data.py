from django.test import TestCase
from django import forms
from django.utils import timezone

from edc.subject.registration.models import RegisteredSubject
from edc.lab.lab_profile.classes import site_lab_profiles
from edc.subject.lab_tracker.classes import site_lab_tracker
from edc.subject.rule_groups.classes import site_rule_groups
from edc.lab.lab_profile.exceptions import AlreadyRegistered as AlreadyRegisteredLabProfile
from edc.subject.appointment.models import Appointment
from edc_constants.constants import NEW, YES, NO, POS, NEG, NOT_REQUIRED

from bhp077.apps.microbiome.app_configuration.classes import MicrobiomeConfiguration
from bhp077.apps.microbiome.constants import LIVE
from bhp077.apps.microbiome_infant.forms import InfantBirthDataForm
from bhp077.apps.microbiome_infant.models import InfantBirthData
from bhp077.apps.microbiome_infant.tests.factories import InfantBirthFactory, InfantVisitFactory
from bhp077.apps.microbiome_infant.visit_schedule import InfantBirthVisitSchedule
from bhp077.apps.microbiome_lab.lab_profiles import MaternalProfile, InfantProfile
from bhp077.apps.microbiome_maternal.tests.factories import MaternalConsentFactory, MaternalLabourDelFactory
from bhp077.apps.microbiome_maternal.tests.factories import MaternalEligibilityFactory, MaternalVisitFactory
from bhp077.apps.microbiome_maternal.tests.factories import PostnatalEnrollmentFactory
from bhp077.apps.microbiome_maternal.visit_schedule import PostnatalEnrollmentVisitSchedule


class BaseTestInfantBirthDataModel(InfantBirthData):
    class Meta:
        app_label = 'microbiome_infant'


class BaseTestInfantBirthDataForm(InfantBirthDataForm):

    class Meta:
        model = BaseTestInfantBirthDataModel
        fields = '__all__'


class TestInfantBirthData(TestCase):

    def setUp(self):
        try:
            site_lab_profiles.register(MaternalProfile())
            site_lab_profiles.register(InfantProfile())
        except AlreadyRegisteredLabProfile:
            pass
        MicrobiomeConfiguration().prepare()
        site_lab_tracker.autodiscover()
        PostnatalEnrollmentVisitSchedule().build()
        site_rule_groups.autodiscover()
        InfantBirthVisitSchedule().build()

        self.maternal_eligibility = MaternalEligibilityFactory()
        self.maternal_consent = MaternalConsentFactory(registered_subject=self.maternal_eligibility.registered_subject)
        self.registered_subject = self.maternal_eligibility.registered_subject

        postnatal = PostnatalEnrollmentFactory(
            registered_subject=self.registered_subject,
            verbal_hiv_status=NEG,
            evidence_hiv_status=YES)
        self.appointment = Appointment.objects.get(
            registered_subject=self.registered_subject, visit_definition__code='2000M')
        maternal_visit = MaternalVisitFactory(appointment=self.appointment)
        maternal_labour_del = MaternalLabourDelFactory(maternal_visit=maternal_visit)
        infant_registered_subject = RegisteredSubject.objects.get(
            subject_type='infant', relative_identifier=self.registered_subject.subject_identifier)
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
            'infant_birth_weight': 3.61,
            'infant_length': 89.97,
            'head_circumference': 39.30,
            'apgar_score': NO,
            'congenital_anomalities': NO
        }

    def test_infant_length(self):
        self.data['infant_birth'] = self.infant_visit.id
        self.data['infant_length'] = 95.62
        self.assertRaises(forms.ValidationError)

    def test_validate_infant_head_cir(self):
        self.data['infant_birth'] = self.infant_visit.id
        self.data['head_circumference'] = 41.23
        self.assertRaises(forms.ValidationError)