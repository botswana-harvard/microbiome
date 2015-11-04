import factory
from django.utils import timezone

from edc_constants.constants import YES, NO, NEG

from bhp077.apps.microbiome_maternal.models import PostnatalEnrollment



class PostnatalEnrollmentFactory(factory.DjangoModelFactory):

    class Meta:
        model = PostnatalEnrollment

    report_datetime = timezone.now()
    registered_subject = factory.SubFactory(RegisteredSubjectFactory)
    citizen = YES
    is_diabetic = YES
    on_tb_treatment = YES
    breastfeed_for_a_year = YES
    instudy_for_a_year = YES
    verbal_hiv_status = POS
    evidence_hiv_status = YES
    valid_regimen = YES
    process_rapid_test = NO
    date_of_rapid_test = timezone.now().date()
