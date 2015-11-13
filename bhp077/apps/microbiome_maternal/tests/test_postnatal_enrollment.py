from django.test import TestCase

from edc.lab.lab_profile.classes import site_lab_profiles
from edc.subject.lab_tracker.classes import site_lab_tracker
from edc.subject.rule_groups.classes import site_rule_groups
from edc.lab.lab_profile.exceptions import AlreadyRegistered as AlreadyRegisteredLabProfile
from edc_constants.choices import YES, NO, POS, NEG, NOT_APPLICABLE

from bhp077.apps.microbiome.app_configuration.classes import MicrobiomeConfiguration
from bhp077.apps.microbiome_maternal.tests.factories import MaternalEligibilityFactory
from bhp077.apps.microbiome_maternal.tests.factories import MaternalConsentFactory
from bhp077.apps.microbiome_lab.lab_profiles import MaternalProfile
from ..visit_schedule import PostnatalEnrollmentVisitSchedule
from .factories import PostnatalEnrollmentFactory
from ..maternal_choices import STILL_BIRTH, LIVE


class TestPostnatalEnroll(TestCase):
    """Test eligibility of a mother for postnatal enrollment."""

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
        self.registered_subject = self.maternal_consent.registered_subject

    def test_breatfeed_yes(self):
        """Test for when breast feeding for a year is yes."""

        postnatal_enrollment = PostnatalEnrollmentFactory(
            registered_subject=self.registered_subject,
            breastfeed_for_a_year=YES
        )
        self.assertTrue(postnatal_enrollment.postnatal_eligible)

    def test_breatfeed_no(self):
        """Test for when breast feeding for a year is no."""

        postnatal_enrollment = PostnatalEnrollmentFactory(
            registered_subject=self.registered_subject,
            breastfeed_for_a_year=NO
        )
        self.assertFalse(postnatal_enrollment.postnatal_eligible)

    def test_on_tb_treatment(self):
        """Test for when on tb treatment."""

        postnatal_enrollment = PostnatalEnrollmentFactory(
            registered_subject=self.registered_subject,
            on_tb_treatment=YES
        )
        self.assertFalse(postnatal_enrollment.postnatal_eligible)

    def test_not_on_tb_treatment(self):
        """Test for when not on tb treatment."""

        postnatal_enrollment = PostnatalEnrollmentFactory(
            registered_subject=self.registered_subject,
            on_tb_treatment=NO
        )
        self.assertTrue(postnatal_enrollment.postnatal_eligible)

    def test_is_diabetic(self):
        """Test for a subject who is diabetic."""

        postnatal_enrollment = PostnatalEnrollmentFactory(
            registered_subject=self.registered_subject,
            is_diabetic=YES
        )
        self.assertFalse(postnatal_enrollment.postnatal_eligible)

    def test_is_not_diabetic(self):
        """Test for a subject who is not diabetic."""

        postnatal_enrollment = PostnatalEnrollmentFactory(
            registered_subject=self.registered_subject,
            is_diabetic=NO
        )
        self.assertTrue(postnatal_enrollment.postnatal_eligible)

    def test_instudy_for_a_year(self):
        """Test for a subject who is in the study for a year."""

        postnatal_enrollment = PostnatalEnrollmentFactory(
            registered_subject=self.registered_subject,
            instudy_for_a_year=YES
        )
        self.assertTrue(postnatal_enrollment.postnatal_eligible)

    def test_not_instudy_for_a_year(self):
        """Test for a subject who is not in the study for a year."""

        postnatal_enrollment = PostnatalEnrollmentFactory(
            registered_subject=self.registered_subject,
            instudy_for_a_year=NO
        )
        self.assertFalse(postnatal_enrollment.postnatal_eligible)

    def test_postpartum_days_more_than_3_days(self):
        """Test for a subject whose postpartum days is more than 3 days."""

        postnatal_enrollment = PostnatalEnrollmentFactory(
            registered_subject=self.registered_subject,
            postpartum_days=4
        )
        self.assertFalse(postnatal_enrollment.postnatal_eligible)

    def test_postpartum_days_less_than_3_days(self):
        """Test for a subject whose postpartum days is less than 3 days."""

        postnatal_enrollment = PostnatalEnrollmentFactory(
            registered_subject=self.registered_subject,
            postpartum_days=2
        )
        self.assertTrue(postnatal_enrollment.postnatal_eligible)

    def test_postpartum_days_equal_3_days(self):
        """Test for a subject whose postpartum days is equals 3 days."""

        postnatal_enrollment = PostnatalEnrollmentFactory(
            registered_subject=self.registered_subject,
            postpartum_days=3
        )
        self.assertTrue(postnatal_enrollment.postnatal_eligible)

    def test_delivery_type_viginal(self):
        """Test for a subject whose delivery type is viginal."""

        postnatal_enrollment = PostnatalEnrollmentFactory(
            registered_subject=self.registered_subject,
            delivery_type=YES
        )
        self.assertTrue(postnatal_enrollment.postnatal_eligible)

    def test_delivery_type_not_viginal(self):
        """Test for a subject whose delivery type is viginal."""

        postnatal_enrollment = PostnatalEnrollmentFactory(
            registered_subject=self.registered_subject,
            delivery_type=NO
        )
        self.assertFalse(postnatal_enrollment.postnatal_eligible)

    def test_still_birth(self):
        """Test for a subject who had a still birth."""

        postnatal_enrollment = PostnatalEnrollmentFactory(
            registered_subject=self.registered_subject,
            live_or_still_birth=STILL_BIRTH
        )
        self.assertFalse(postnatal_enrollment.postnatal_eligible)

    def test_live_birth(self):
        """Test for a subject who had a live birth."""

        postnatal_enrollment = PostnatalEnrollmentFactory(
            registered_subject=self.registered_subject,
            live_or_still_birth=LIVE
        )
        self.assertTrue(postnatal_enrollment.postnatal_eligible)

    def test_gestation_before_birth_below_37(self):
        """Test for a subject whose gestation before birth is below 37."""

        postnatal_enrollment = PostnatalEnrollmentFactory(
            registered_subject=self.registered_subject,
            gestation_before_birth=36
        )
        self.assertFalse(postnatal_enrollment.postnatal_eligible)

    def test_gestation_before_birth_equal_37(self):
        """Test for a subject whose gestation before birth is equals to 37."""

        postnatal_enrollment = PostnatalEnrollmentFactory(
            registered_subject=self.registered_subject,
            gestation_before_birth=37
        )
        self.assertTrue(postnatal_enrollment.postnatal_eligible)

    def test_gestation_before_birth_above_37(self):
        """Test for a subject whose gestation before birth is above 37."""

        postnatal_enrollment = PostnatalEnrollmentFactory(
            registered_subject=self.registered_subject,
            gestation_before_birth=38
        )
        self.assertTrue(postnatal_enrollment.postnatal_eligible)

    def test_pos_has_evidence_valid_regimen_valid_regimen_duration(self):
        """Test for a subject who is positive, has evidence, valid regimen, valid regimen duration."""

        postnatal_enrollment = PostnatalEnrollmentFactory(
            registered_subject=self.registered_subject,
            verbal_hiv_status=POS,
            evidence_hiv_status=YES,
            valid_regimen=YES,
            valid_regimen_duration=YES
        )
        self.assertTrue(postnatal_enrollment.postnatal_eligible)

    def test_pos_has_evidence_no_valid_regimen(self):
        """Test for a subject who is positive, has evidence, no valid regimen."""

        postnatal_enrollment = PostnatalEnrollmentFactory(
            registered_subject=self.registered_subject,
            verbal_hiv_status=POS,
            evidence_hiv_status=YES,
            valid_regimen=NO,
        )
        self.assertFalse(postnatal_enrollment.postnatal_eligible)

    def test_pos_has_evidence_valid_regimen_unvalid_regimen_duration(self):
        """Test for a subject who is positive, has evidence, valid regimen, unvalid regimen duration."""

        postnatal_enrollment = PostnatalEnrollmentFactory(
            registered_subject=self.registered_subject,
            verbal_hiv_status=POS,
            evidence_hiv_status=YES,
            valid_regimen=YES,
            valid_regimen_duration=NO
        )
        self.assertFalse(postnatal_enrollment.postnatal_eligible)

    def test_negative_with_evidence(self):
        """Test for a subject whose verbal hiv status is negative and has evidence."""

        postnatal_enrollment = PostnatalEnrollmentFactory(
            registered_subject=self.registered_subject,
            verbal_hiv_status=NEG,
            evidence_hiv_status=YES
        )
        self.assertTrue(postnatal_enrollment.postnatal_eligible)

    def test_negative_with_no_evidence(self):
        """Test for a subject whose verbal hiv status is negative and has no evidence."""

        postnatal_enrollment = PostnatalEnrollmentFactory(
            registered_subject=self.registered_subject,
            verbal_hiv_status=NEG,
            evidence_hiv_status=NO,
            valid_regimen=NOT_APPLICABLE,
            process_rapid_test=YES,
            rapid_test_result=NEG
        )
        self.assertTrue(postnatal_enrollment.postnatal_eligible)

    def test_verbal_hiv_status_neg_with_no_evidence(self):
        """Test for a subject whose verbal hiv status is NEG and has no evidence, rapid test result POS."""

        postnatal_enrollment = PostnatalEnrollmentFactory(
            registered_subject=self.registered_subject,
            verbal_hiv_status=NEG,
            evidence_hiv_status=NO,
            valid_regimen=NOT_APPLICABLE,
            process_rapid_test=YES,
            rapid_test_result=POS
        )
        self.assertFalse(postnatal_enrollment.postnatal_eligible)

    def test_verbal_hiv_status_never_tested_for_HIV_1(self):
        """Test for a subject whose verbal hiv status is Never tested for HIV and rapid test result is NEG."""

        postnatal_enrollment = PostnatalEnrollmentFactory(
            registered_subject=self.registered_subject,
            verbal_hiv_status="Never tested for HIV",
            valid_regimen=NOT_APPLICABLE,
            process_rapid_test=YES,
            rapid_test_result=NEG
        )
        self.assertTrue(postnatal_enrollment.postnatal_eligible)

    def test_verbal_hiv_status_never_tested_for_HIV_2(self):
        """Test for a subject whose verbal hiv status is Never tested for HIV rapid test result POS."""

        postnatal_enrollment = PostnatalEnrollmentFactory(
            registered_subject=self.registered_subject,
            verbal_hiv_status="Never tested for HIV",
            valid_regimen=NOT_APPLICABLE,
            process_rapid_test=YES,
            rapid_test_result=POS
        )
        self.assertFalse(postnatal_enrollment.postnatal_eligible)

    def test_verbal_hiv_status_unknown_rapid_test_result_neg(self):
        """Test for a subject whose verbal hiv status is unknown and rapid test result NEG."""

        postnatal_enrollment = PostnatalEnrollmentFactory(
            registered_subject=self.registered_subject,
            verbal_hiv_status="Unknown",
            valid_regimen=NOT_APPLICABLE,
            process_rapid_test=YES,
            rapid_test_result=NEG
        )
        self.assertTrue(postnatal_enrollment.postnatal_eligible)

    def test_verbal_hiv_status_unknown_rapid_test_result_pos(self):
        """Test for a subject whose verbal hiv status is unknown and rapid test result POS."""

        postnatal_enrollment = PostnatalEnrollmentFactory(
            registered_subject=self.registered_subject,
            verbal_hiv_status="Unknown",
            valid_regimen=NOT_APPLICABLE,
            process_rapid_test=YES,
            rapid_test_result=POS
        )
        self.assertFalse(postnatal_enrollment.postnatal_eligible)

    def test_verbal_hiv_status_refused_to_answer_rapid_test_result_pos(self):
        """Test for a subject whose verbal hiv status is refused to answer and rapid test result POS."""

        postnatal_enrollment = PostnatalEnrollmentFactory(
            registered_subject=self.registered_subject,
            verbal_hiv_status="Refused to answer",
            valid_regimen=NOT_APPLICABLE,
            process_rapid_test=YES,
            rapid_test_result=POS
        )
        self.assertFalse(postnatal_enrollment.postnatal_eligible)

    def test_verbal_hiv_status_refused_to_answer_rapid_test_result_neg(self):
        """Test for a subject whose verbal hiv status is refused to answer and rapid test result NEG."""

        postnatal_enrollment = PostnatalEnrollmentFactory(
            registered_subject=self.registered_subject,
            verbal_hiv_status="Refused to answer",
            valid_regimen=NOT_APPLICABLE,
            process_rapid_test=YES,
            rapid_test_result=NEG
        )
        self.assertTrue(postnatal_enrollment.postnatal_eligible)