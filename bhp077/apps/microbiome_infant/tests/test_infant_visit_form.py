from django.test import TestCase
from django.utils import timezone

from bhp077.apps.microbiome_infant.models import InfantVisit
from bhp077.apps.microbiome_infant.forms import InfantVisitForm

from django.test import TestCase
from django.utils import timezone

from edc.subject.registration.models import RegisteredSubject
from edc.entry_meta_data.models import ScheduledEntryMetaData, RequisitionMetaData
from edc.lab.lab_profile.classes import site_lab_profiles
from edc.subject.lab_tracker.classes import site_lab_tracker
from edc.subject.rule_groups.classes import site_rule_groups
from edc.lab.lab_profile.exceptions import AlreadyRegistered as AlreadyRegisteredLabProfile
from edc.subject.appointment.models import Appointment
from edc_constants.constants import NEW, YES, NO, POS, NEG, NOT_REQUIRED

from bhp077.apps.microbiome.constants import LIVE
from bhp077.apps.microbiome.app_configuration.classes import MicrobiomeConfiguration
from bhp077.apps.microbiome_maternal.tests.factories import (MaternalEligibilityFactory, AntenatalEnrollmentFactory,
    MaternalVisitFactory)
from bhp077.apps.microbiome_maternal.tests.factories import MaternalConsentFactory, MaternalLabourDelFactory
from bhp077.apps.microbiome_maternal.tests.factories import PostnatalEnrollmentFactory, SexualReproductiveHealthFactory
from bhp077.apps.microbiome_lab.lab_profiles import MaternalProfile, InfantProfile
from bhp077.apps.microbiome_maternal.models import PostnatalEnrollment

from bhp077.apps.microbiome_maternal.visit_schedule import AntenatalEnrollmentVisitSchedule, PostnatalEnrollmentVisitSchedule
from bhp077.apps.microbiome_infant.visit_schedule import InfantBirthVisitSchedule
from bhp077.apps.microbiome_infant.tests.factories import InfantBirthFactory, InfantBirthDataFactory, InfantVisitFactory
from bhp077.apps.microbiome_infant.models import InfantBirth

from bhp077.apps.microbiome_lab.models import Panel, AliquotType


class TestInfantVisitForm(TestCase):


    def setUp(self):
        try:
            site_lab_profiles.register(MaternalProfile())
            site_lab_profiles.register(InfantProfile())
        except AlreadyRegisteredLabProfile:
            pass
        MicrobiomeConfiguration().prepare()
        site_lab_tracker.autodiscover()
        AntenatalEnrollmentVisitSchedule().build()
        PostnatalEnrollmentVisitSchedule().build()
        site_rule_groups.autodiscover()
        InfantBirthVisitSchedule().build()

        self.maternal_eligibility = MaternalEligibilityFactory()
        self.maternal_consent = MaternalConsentFactory(registered_subject=self.maternal_eligibility.registered_subject)
        self.registered_subject = self.maternal_consent.registered_subject

        post = PostnatalEnrollmentFactory(
            registered_subject=self.registered_subject,
            verbal_hiv_status=POS,
            evidence_hiv_status=YES,
        )
        appointment = Appointment.objects.get(
            registered_subject=self.registered_subject, visit_definition__code='2000M'
        )
        maternal_visit = MaternalVisitFactory(appointment=appointment)
        maternal_labour_del = MaternalLabourDelFactory(maternal_visit=maternal_visit)

        registered_subject_infant = RegisteredSubject.objects.get(
            subject_type='infant', relative_identifier=self.registered_subject.subject_identifier
        )
        InfantBirthFactory(
            registered_subject=registered_subject_infant,
            maternal_labour_del=maternal_labour_del,
        )
        self.appointment = Appointment.objects.get(
            registered_subject=registered_subject_infant,
            visit_definition__code='2000'
        )
    def test_validate_reason_death_valid(self):
        data = {
            'reason': 'death', 'survival_status': 'DEAD',
            'study_status': 'offstudy', 'appointment':self.appointment.id,
            'info_source': 'other_doctor', 'information_provider': 'MOTHER',
            'report_datetime': timezone.now(),
            'date_last_alive':timezone.now().date()
        }
        visit_form = InfantVisitForm(data=data)
        self.assertTrue(visit_form.is_valid())

    def test_validate_reason_death_not_valid(self):
        data = {
            'reason': 'death', 'survival_status': 'ALIVE',
            'study_status': 'offstudy', 'appointment':self.appointment.id,
            'info_source': 'other_doctor', 'information_provider': 'MOTHER',
            'report_datetime': timezone.now(),
        }
        visit_form = InfantVisitForm(data=data)
        self.assertIn(u'You should select Deceased for survival status.', visit_form.errors.get('__all__'))

    def test_validate_reason_death_not_valid1(self):
        data = {
            'reason': 'death', 'survival_status': 'DEAD',
            'study_status': 'onstudy', 'appointment':self.appointment.id,
            'info_source': 'other_doctor', 'information_provider': 'MOTHER',
            'report_datetime': timezone.now(),
        }
        visit_form = InfantVisitForm(data=data)
        self.assertIn(u"You should select offstudy for the participant's current study status.", visit_form.errors.get('__all__'))

    def test_validate_reason_lost_and_completed(self):
        data = {
            'reason': 'lost', 'survival_status': 'DEAD',
            'study_status': 'onstudy', 'appointment':self.appointment.id,
            'info_source': 'other_doctor', 'information_provider': 'MOTHER',
            'report_datetime': timezone.now(),
            'date_last_alive':timezone.now().date(),
        }
        visit_form = InfantVisitForm(data=data)
        self.assertIn(u"You should select offstudy for the participant's current study status.", visit_form.errors.get('__all__'))

    def test_validate_reason_missed_valid(self):
        data = {
            'reason': 'missed', 'survival_status': 'DEAD',
            'study_status': 'onstudy', 'appointment':self.appointment.id,
            'information_provider': 'MOTHER',
            'report_datetime': timezone.now(),
            'reason_missed': 'I was in the cattle post.',
            'date_last_alive':timezone.now().date(),
        }
        visit_form = InfantVisitForm(data=data)
        self.assertTrue(visit_form.is_valid())


    def test_validate_reason_missed_not_valid(self):
        data = {
            'reason': 'missed', 'survival_status': 'DEAD',
            'study_status': 'onstudy', 'appointment':self.appointment.id,
            'info_source': 'other_doctor', 'information_provider': 'MOTHER',
            'report_datetime': timezone.now(),
        }
        visit_form = InfantVisitForm(data=data)
        self.assertIn(u"Provide reason scheduled visit was missed.", visit_form.errors.get('__all__'))

    def test_validate_survival_status(self):
        data = {
            'reason': 'scheduled', 'survival_status': 'ALIVE',
            'study_status': 'onstudy', 'appointment':self.appointment.id,
            'info_source': 'other_doctor', 'information_provider': 'MOTHER',
            'report_datetime': timezone.now(),
        }
        visit_form = InfantVisitForm(data=data)
        self.assertIn(u'Provide Date last known alive.', visit_form.errors.get('__all__'))