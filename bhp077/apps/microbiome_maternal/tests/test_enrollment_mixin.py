from datetime import date
from django.test import TestCase
from django.utils import timezone
from django.db import models

from edc.lab.lab_profile.classes import site_lab_profiles
from edc.lab.lab_profile.exceptions import AlreadyRegistered as AlreadyRegisteredLabProfile
from edc.subject.registration.models import RegisteredSubject
from edc.subject.lab_tracker.classes import site_lab_tracker
from edc.subject.rule_groups.classes import site_rule_groups
from edc_constants.choices import POS, YES, NO, NEG, NOT_APPLICABLE
from edc_constants.constants import NEVER

from bhp077.apps.microbiome.app_configuration.classes import MicrobiomeConfiguration
from bhp077.apps.microbiome_lab.lab_profiles import MaternalProfile
from bhp077.apps.microbiome_maternal.tests.factories import (MaternalEligibilityFactory,
                                                             MaternalConsentFactory,
                                                             SpecimenConsentFactory)
from bhp077.apps.microbiome_maternal.forms import BaseEnrollmentForm
from bhp077.apps.microbiome_maternal.models.enrollment_mixin import EnrollmentMixin


class EnrollTestModel(EnrollmentMixin):

    registered_subject = models.OneToOneField(RegisteredSubject, null=True)

    report_datetime = models.DateTimeField(
        default=timezone.now())

    def save_common_fields_to_postnatal_enrollment(self):
        pass

    def save(self, *args, **kwargs):
        self.is_eligible = True
        super(EnrollTestModel, self).save(*args, **kwargs)

    class Meta:
        app_label = 'microbiome_maternal'


class BaseEnrollTestForm(BaseEnrollmentForm):

    class Meta:
        model = EnrollTestModel
        fields = '__all__'


class TestEnrollmentMixin(TestCase):
    """Test eligibility of a mother for antenatal enrollment."""

    def setUp(self):
        try:
            site_lab_profiles.register(MaternalProfile())
        except AlreadyRegisteredLabProfile:
            pass
        MicrobiomeConfiguration().prepare()
        site_lab_tracker.autodiscover()
        site_rule_groups.autodiscover()
        self.maternal_eligibility = MaternalEligibilityFactory()
        self.maternal_consent = MaternalConsentFactory(
            registered_subject=self.maternal_eligibility.registered_subject)
        self.registered_subject = self.maternal_consent.registered_subject
        self.specimen_consent = SpecimenConsentFactory(registered_subject=self.registered_subject)
        self.data = {
            'registered_subject': self.registered_subject.id,
            'report_datetime': timezone.now(),
            'is_diabetic': NO,
            'on_tb_tx': NO,
            'will_breastfeed': NO,
            'will_remain_onstudy': NO,
            'week32_test': NO,
            'week32_result': '',
            'current_hiv_status': POS,
            'evidence_hiv_status': NO,
            'valid_regimen': NO,
            'valid_regimen_duration': NOT_APPLICABLE,
            'rapid_test_done': NO,
            'rapid_test_date': '',
            'rapid_test_result': '',
        }

    def test_process_rapid_yes_date_req(self):
        """If rapid test was processed, test date was processed is required"""
        self.data['rapid_test_done'] = YES
        form = BaseEnrollTestForm(data=self.data)
        self.assertIn('You indicated that a rapid test was processed. Please provide the date.',
                      form.errors.get('__all__'))

    def test_process_rapid_no_date_req(self):
        """If rapid test was NOT processed, test date was processed is  NOT required"""
        self.data['rapid_test_done'] = NO
        self.data['rapid_test_date'] = date.today()
        form = BaseEnrollTestForm(data=self.data)
        self.assertIn('You indicated that a rapid test was NOT processed, yet rapid test date was provided. '
                      'Please correct.', form.errors.get('__all__'))

    def test_process_rapid_na_date_req(self):
        """If rapid test was NOT processed, test date was processed is  NOT required"""
        self.data['rapid_test_done'] = NOT_APPLICABLE
        self.data['rapid_test_date'] = date.today()
        form = BaseEnrollTestForm(data=self.data)
        self.assertIn('You indicated that a rapid test was NOT processed, yet rapid test date was provided. '
                      'Please correct.', form.errors.get('__all__'))

    def test_process_rapid_yes_result_req(self):
        """If rapid test was processed, test result was processed is required"""
        self.data['rapid_test_done'] = YES
        self.data['rapid_test_date'] = date.today()
        form = BaseEnrollTestForm(data=self.data)
        self.assertIn('You indicated that a rapid test was processed. Please provide a result.',
                      form.errors.get('__all__'))

    def test_process_rapid_no_result_not_req(self):
        """If rapid test was NOT processed, test result was processed is NOT required"""
        self.data['rapid_test_done'] = NO
        self.data['rapid_test_result'] = POS
        form = BaseEnrollTestForm(data=self.data)
        self.assertIn('You indicated that a rapid test was NOT processed, yet rapid test result was provided. '
                      'Please correct.', form.errors.get('__all__'))

    def test_process_rapid_na_result_not_req(self):
        """If rapid test was NOT processed, test result was processed is NOT required"""
        self.data['rapid_test_done'] = NOT_APPLICABLE
        self.data['rapid_test_result'] = NEG
        form = BaseEnrollTestForm(data=self.data)
        self.assertIn('You indicated that a rapid test was NOT processed, yet rapid test result was provided. '
                      'Please correct.', form.errors.get('__all__'))

    def test_regimen_duration_na(self):
        self.data['valid_regimen'] = YES
        self.data['valid_regimen_duration'] = NOT_APPLICABLE
        form = BaseEnrollTestForm(data=self.data)
        self.assertIn('You have indicated that the participant is on ARV. Regimen validity period'
                      ' CANNOT be \'Not Applicable\'. Please correct.', form.errors.get('__all__'))

    def test_regimen_duration_yes(self):
        self.data['valid_regimen'] = NO
        self.data['valid_regimen_duration'] = YES
        form = BaseEnrollTestForm(data=self.data)
        self.assertIn('You have indicated that there are no records of Participant taking ARVs. '
                      'Regimen validity period should be \'Not Applicable\'. '
                      'Please correct.', form.errors.get('__all__'))

    def test_regimen_duration_no(self):
        self.data['valid_regimen'] = NO
        self.data['valid_regimen_duration'] = NO
        form = BaseEnrollTestForm(data=self.data)
        self.assertIn('You have indicated that there are no records of Participant taking ARVs. '
                      'Regimen validity period should be \'Not Applicable\'. '
                      'Please correct.', form.errors.get('__all__'))

    def test_hiv_evidence_pos(self):
        self.data['evidence_hiv_status'] = NOT_APPLICABLE
        form = BaseEnrollTestForm(data=self.data)
        self.assertIn('You have indicated that the participant is Positive, Evidence of HIV '
                      'result CANNOT be \'Not Applicable\'. Please correct.', form.errors.get('__all__'))

    def test_hiv_evidence_pos_reg_na(self):
        self.data['valid_regimen'] = NOT_APPLICABLE
        form = BaseEnrollTestForm(data=self.data)
        self.assertIn('You have indicated that the participant is Positive, \'do records show that'
                      ' participant takes ARVs\' cannot be \'Not Applicable\'.', form.errors.get('__all__'))

    def test_hiv_evidence_neg(self):
        self.data['current_hiv_status'] = NEG
        self.data['evidence_hiv_status'] = NOT_APPLICABLE
        form = BaseEnrollTestForm(data=self.data)
        self.assertIn('You have indicated that the participant is Negative, Evidence of HIV '
                      'result CANNOT be \'Not Applicable\'. Please correct.', form.errors.get('__all__'))

    def test_sample_filled_before_enrollment(self):
        self.specimen_consent.delete()
        form = BaseEnrollTestForm(data=self.data)
        self.assertIn('Please ensure to save the Specimen Consent before completing Enrollment',
                      form.errors.get('__all__'))

    def test_pos_with_evidence_and_do_rapid_test(self):
        self.data['evidence_hiv_status'] = YES
        self.data['rapid_test_done'] = YES
        form = BaseEnrollTestForm(data=self.data)
        self.assertIn('DO NOT PROCESS RAPID TEST. PARTICIPANT IS POS and HAS EVIDENCE.',
                      form.errors.get('__all__'))

    def test_participant_never_tested(self):
        self.data['current_hiv_status'] = NEVER
        self.data['evidence_hiv_status'] = NOT_APPLICABLE
        self.data['valid_regimen'] = NOT_APPLICABLE
        form = BaseEnrollTestForm(data=self.data)
        self.assertIn('Participant current HIV status is {}. You must conduct HIV rapid testing '
                      'today to continue with the eligibility screen'.format(
                          self.data['current_hiv_status']), form.errors.get('__all__'))

    def test_results_comparison(self):
        self.data['week32_test'] = YES
        self.data['week32_result'] = NEG
        form = BaseEnrollTestForm(data=self.data)
        self.assertIn(
            'The current hiv status and result at 32weeks should be the same!',
            form.errors.get('__all__'))

    def test_tested_at_32weeks_no_result(self):
        self.data['week32_test'] = YES
        self.data['week32_result'] = None
        form = BaseEnrollTestForm(data=self.data)
        self.assertIn('Please provide test result at week 32.', form.errors.get('__all__'))

    def test_not_tested_at_32weeks_results_given(self):
        self.data['week32_result'] = POS
        form = BaseEnrollTestForm(data=self.data)
        self.assertIn(
            'You mentioned testing was not done at 32weeks yet provided a '
            'test result.', form.errors.get('__all__'))