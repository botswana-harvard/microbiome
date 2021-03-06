import factory

from django.utils import timezone

from microbiome.apps.mb_maternal.models import MaternalOffStudy

from .maternal_visit_factory import MaternalVisitFactory


class MaternalOffStudyFactory(factory.DjangoModelFactory):

    class Meta:
        model = MaternalOffStudy

    offstudy_date = timezone.now().date()

    maternal_visit = factory.SubFactory(MaternalVisitFactory)
