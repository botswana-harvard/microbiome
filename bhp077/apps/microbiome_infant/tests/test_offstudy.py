from django.test import TestCase
from django.utils import timezone
from datetime import date

from edc.subject.registration.models import RegisteredSubject
from edc.entry_meta_data.models import ScheduledEntryMetaData, RequisitionMetaData
from edc.lab.lab_profile.classes import site_lab_profiles
from edc.subject.lab_tracker.classes import site_lab_tracker
from edc.subject.rule_groups.classes import site_rule_groups
from edc.lab.lab_profile.exceptions import AlreadyRegistered as AlreadyRegisteredLabProfile
from edc.subject.appointment.models import Appointment
from edc_constants.constants import NEW, YES, NO, POS, NEG, NOT_REQUIRED, OFF_STUDY

from bhp077.apps.microbiome.constants import LIVE
from bhp077.apps.microbiome.app_configuration.classes import MicrobiomeConfiguration
from bhp077.apps.microbiome_maternal.tests.factories import (MaternalEligibilityFactory, AntenatalEnrollmentFactory,
    MaternalVisitFactory)
from bhp077.apps.microbiome_maternal.tests.factories import MaternalConsentFactory, MaternalLabourDelFactory
from bhp077.apps.microbiome_maternal.tests.factories import PostnatalEnrollmentFactory, ReproductiveHealthFactory
from bhp077.apps.microbiome_lab.lab_profiles import MaternalProfile, InfantProfile
from bhp077.apps.microbiome_maternal.models import PostnatalEnrollment

from bhp077.apps.microbiome_maternal.visit_schedule import AntenatalEnrollmentVisitSchedule, PostnatalEnrollmentVisitSchedule
from bhp077.apps.microbiome_infant.visit_schedule import InfantBirthVisitSchedule
from bhp077.apps.microbiome_infant.tests.factories import (InfantBirthFactory, InfantBirthDataFactory,
                                                           InfantVisitFactory, InfantOffStudyFactory
                                                           )
from bhp077.apps.microbiome_infant.models import InfantBirth
from bhp077.apps.microbiome.constants import MIN_AGE_OF_CONSENT

from ..forms import InfantOffStudyForm


class TestOffStudy(TestCase):

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
        self.registered_subject = self.maternal_eligibility.registered_subject
        self.maternal_consent = MaternalConsentFactory(
            registered_subject=self.registered_subject)

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
        self.infant_registered_subject = RegisteredSubject.objects.get(
            relative_identifier=self.registered_subject.subject_identifier,
            subject_type='infant')
        self.infant_birth = InfantBirthFactory(
            registered_subject=self.infant_registered_subject,
            maternal_labour_del=maternal_labour_del)
        self.infant_appointment = Appointment.objects.get(
            registered_subject=self.infant_registered_subject,
            visit_definition__code='2000')

        self.data = {
            'registered_subject': self.registered_subject.id,
            'reason': 'not_{}'.format(MIN_AGE_OF_CONSENT),
            'has_scheduled_data': YES,
            'infant_visit': None,
            'offstudy_date': timezone.now().date(),
        }

    def test_offstudy_meta_data_created_on_visit(self):
        self.infant_visit = InfantVisitFactory(
            appointment=self.infant_appointment,
            reason=OFF_STUDY)
        self.assertEqual(
            ScheduledEntryMetaData.objects.filter(
                entry_status=NEW,
                entry__app_label='microbiome_infant',
                entry__model_name='infantoffstudy',
                appointment=self.infant_appointment).count(), 1)

    def test_offstudy2(self):
        self.infant_visit = InfantVisitFactory(
            appointment=self.infant_appointment,
            reason=OFF_STUDY)
        InfantOffStudyFactory(
            report_datetime=timezone.now(),
            registered_subject=self.infant_appointment.registered_subject,
            infant_visit=self.infant_visit)
        self.assertEqual(
            Appointment.objects.filter(
                registered_subject=self.infant_registered_subject).count(), 1)

    def test_validate_offstudy_date(self):

        self.infant_visit = InfantVisitFactory(
            appointment=self.infant_appointment,
            reason=OFF_STUDY)
        self.data['infant_visit'] = self.infant_visit.id
        self.data['offstudy_date'] = date(2015, 10, 6)
        offstudy_form = InfantOffStudyForm(data=self.data)
        offstudy_form.is_valid()
        self.assertIn("Off study date cannot be before consent date", offstudy_form.errors.get("__all__"))
