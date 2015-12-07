import factory

from django.conf import settings
from django.utils import timezone

from edc.subject.registration.tests.factories import RegisteredSubjectFactory
from edc_constants.constants import YES

from bhp077.apps.microbiome_maternal.models import SpecimenConsent


class SpecimenConsentFactory(factory.DjangoModelFactory):

    class Meta:
        model = SpecimenConsent

    registered_subject = factory.SubFactory(RegisteredSubjectFactory)
    consent_datetime = timezone.now()
    language = settings.LANGUAGES
    may_store_samples = YES
    is_literate = YES
