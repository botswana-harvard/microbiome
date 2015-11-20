from django.test import TestCase
from django.utils import timezone
from datetime import date

from edc.subject.registration.models import RegisteredSubject
from edc.entry_meta_data.models import ScheduledEntryMetaData
from edc.lab.lab_profile.classes import site_lab_profiles
from edc.subject.lab_tracker.classes import site_lab_tracker
from edc.subject.rule_groups.classes import site_rule_groups
from edc.lab.lab_profile.exceptions import AlreadyRegistered as AlreadyRegisteredLabProfile
from edc.subject.appointment.models import Appointment
from edc_constants.constants import NEW, YES, NO, POS, NEG, NOT_REQUIRED

from bhp077.apps.microbiome.constants import LIVE
from bhp077.apps.microbiome.app_configuration.classes import MicrobiomeConfiguration
from bhp077.apps.microbiome_maternal.tests.factories import \
    (MaternalEligibilityFactory, AntenatalEnrollmentFactory,
    MaternalVisitFactory)
from bhp077.apps.microbiome_maternal.tests.factories import MaternalConsentFactory
from bhp077.apps.microbiome_maternal.tests.factories import\
    (PostnatalEnrollmentFactory, SexualReproductiveHealthFactory, MaternalOffStudyFactory)
from bhp077.apps.microbiome_lab.lab_profiles import MaternalProfile
from bhp077.apps.microbiome_maternal.models import PostnatalEnrollment
from bhp077.apps.microbiome_maternal.forms import MaternalObstericalHistoryForm

from ..visit_schedule import AntenatalEnrollmentVisitSchedule, PostnatalEnrollmentVisitSchedule


class TestMaternalObstericalHistoryForm(TestCase):

    def setUp(self):
        try:
            site_lab_profiles.register(MaternalProfile())
        except AlreadyRegisteredLabProfile:
            pass
        MicrobiomeConfiguration().prepare()
        site_lab_tracker.autodiscover()
        AntenatalEnrollmentVisitSchedule().build()
        PostnatalEnrollmentVisitSchedule().build()
        site_rule_groups.autodiscover()

        self.maternal_eligibility = MaternalEligibilityFactory()
        self.maternal_consent = MaternalConsentFactory(registered_subject=self.maternal_eligibility.registered_subject)
        self.registered_subject = self.maternal_consent.registered_subject

        PostnatalEnrollmentFactory(
            registered_subject=self.registered_subject,
            verbal_hiv_status=NEG,
            evidence_hiv_status=YES,
        )
        appointment = Appointment.objects.get(
            registered_subject=self.registered_subject, visit_definition__code='1000M'
        )

        self.maternal_visit = MaternalVisitFactory(appointment=appointment, reason='scheduled')

        self.data = {
            'report_datetime': timezone.now(),
            'maternal_visit': self.maternal_visit.id,
            'pregs_24wks_or_more': 1,
            'lost_before_24wks': 2,
            'lost_after_24wks': 2,
            'live_children': 2,
            'children_died_b4_5yrs': 1
        }

    def test_maternal_obsterical_history_form_valid(self):
        mob = MaternalObstericalHistoryForm(data=self.data)
        self.assertTrue(mob.is_valid())

    def test_maternal_obsterical_history_form_valid1(self):
        self.data = {
            'report_datetime': timezone.now(),
            'maternal_visit': self.maternal_visit.id,
            'pregs_24wks_or_more': 1,
            'lost_before_24wks': 0,
            'lost_after_24wks': 0,
            'live_children': 1,
            'children_died_b4_5yrs': 0
        }
        mob = MaternalObstericalHistoryForm(data=self.data)
        print mob.errors
        self.assertTrue(mob.is_valid())


    def test_maternal_obsterical_history_children_died_b4_5yrs_invalid(self):
        self.data['children_died_b4_5yrs'] = -1
        mob = MaternalObstericalHistoryForm(data=self.data)
        self.assertIn(
            u"How many of the participant's children died after birth before 5 years of age?. Provide value greater than zero.",
            mob.errors.get('__all__')
        )

    def test_maternal_obsterical_history_children_died_b4_5yrs_valid(self):
        self.data['pregs_24wks_or_more'] = 2
        self.data['lost_after_24wks'] = 2
        self.data['children_died_b4_5yrs'] = 2
        mob = MaternalObstericalHistoryForm(data=self.data)
        self.assertTrue(mob.is_valid())

    def test_maternal_obsterical_history_live_children_invalid(self):
        self.data['live_children'] = -1
        mob = MaternalObstericalHistoryForm(data=self.data)
        self.assertIn(
            u"How many other living children does the participant currently have (excluding baby to be enrolled in the "
            u"study.) Provide value greater than zero.", mob.errors.get('__all__')
        )

    def test_maternal_obsterical_history_live_children_valid(self):
        self.data['live_children'] = 2
        mob = MaternalObstericalHistoryForm(data=self.data)
        self.assertTrue(mob.is_valid())

    def test_maternal_obsterical_history_pregs_24wks_or_more_invalid(self):
        self.data['pregs_24wks_or_more'] = -1
        self.data['lost_after_24wks'] = 2
        self.data['children_died_b4_5yrs'] = 2
        mob = MaternalObstericalHistoryForm(data=self.data)
        self.assertIn(u"Number of pregnancies at least 24 weeks, should be greater than zero.", mob.errors.get('__all__'))

    def test_maternal_obsterical_history_pregs_24wks_or_more_valid(self):
        self.data['pregs_24wks_or_more'] = 2
        self.data['lost_after_24wks'] = 2
        self.data['children_died_b4_5yrs'] = 2
        mob = MaternalObstericalHistoryForm(data=self.data)
        self.assertTrue(mob.is_valid())