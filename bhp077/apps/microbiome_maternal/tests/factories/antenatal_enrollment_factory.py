import factory

from django.utils import timezone

from edc_constants.choices import POS, YES, NO

from edc.subject.registration.tests.factories import RegisteredSubjectFactory

from bhp077.apps.microbiome_maternal.models import AntenatalEnrollment


class AntenatalEnrollmentFactory(factory.DjangoModelFactory):

    class Meta:
        model = AntenatalEnrollment

    gestation_wks = 36
    registered_subject = factory.SubFactory(RegisteredSubjectFactory)
    is_diabetic = NO
    on_tb_tx = NO
    will_breastfeed = YES
    will_remain_onstudy = YES
    week32_test = YES
    verbal_hiv_status = POS
    evidence_hiv_status = YES
    valid_regimen = YES
    valid_regimen_duration = YES
    report_datetime = timezone.now()
