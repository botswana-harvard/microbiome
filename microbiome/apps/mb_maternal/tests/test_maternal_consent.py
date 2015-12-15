from django.test import TestCase

from edc.lab.lab_profile.classes import site_lab_profiles
from edc.subject.lab_tracker.classes import site_lab_tracker
from edc.subject.rule_groups.classes import site_rule_groups
from edc.lab.lab_profile.exceptions import AlreadyRegistered as AlreadyRegisteredLabProfile

from microbiome.apps.mb.app_configuration.classes import MicrobiomeConfiguration
from microbiome.apps.mb_lab.lab_profiles import MaternalProfile
from microbiome.apps.mb_maternal.forms import MaternalConsentForm

from .factories import MaternalEligibilityFactory, MaternalConsentFactory


class TestMaternalConsent(TestCase):

    def setUp(self):
        try:
            site_lab_profiles.register(MaternalProfile())
        except AlreadyRegisteredLabProfile:
            pass
        MicrobiomeConfiguration().prepare()
        site_lab_tracker.autodiscover()
        site_rule_groups.autodiscover()
        self.maternal_eligibility = MaternalEligibilityFactory()

    def test_identity_wrong_gender(self):
        """Test that Omang number reflects the correct gender digit."""
        consent = MaternalConsentFactory(
            identity='123411234', confirm_identity='123411234',
            registered_subject=self.maternal_eligibility.registered_subject)
        consent_form = MaternalConsentForm(data=consent.__dict__)
        errors = ''.join(consent_form.errors.get('__all__'))
        self.assertIn('Identity provided indicates participant is Male.', errors)