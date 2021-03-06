import factory

from datetime import date

from edc_constants.choices import NO

from microbiome.apps.mb_maternal.models import MaternalLocator

from .maternal_visit_factory import MaternalVisitFactory


class MaternalLocatorFactory(factory.DjangoModelFactory):

    class Meta:
        model = MaternalLocator

    maternal_visit = factory.SubFactory(MaternalVisitFactory)
    has_caretaker = NO
    date_signed = date.today()
