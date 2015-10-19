from django.db.models.signals import post_save
from django.db import transaction
from django.dispatch import receiver
from edc_constants.constants import POS

from ..constants import NOT_ENROLLED
from ..exceptions import CreateInfantEligibilityError
from ..models import MaternalEligibility, InfantEligibility, SubjectConsent


@receiver(post_save, weak=False, dispatch_uid='maternal_eligibility_post_save')
def maternal_eligibility_post_save(sender, instance, raw, created, using, update_fields, **kwargs):
    """Creates the Infant Eligibility recored to match the number in MaternalEligibility.live_infants.
    Only the foreign key to MaternalEligibility. The user will need to open the form and populate all
    other fields accordingly, before proceeding."""
    if not raw:
        if isinstance(instance, MaternalEligibility):
            num_live_infants = instance.live_infants
            if instance.mother_hiv_result == POS and instance.enrollment_status != NOT_ENROLLED:
                try:
                    with transaction.atomic():
                        for _ in list(range(0, num_live_infants)):
                            InfantEligibility.objects.create(maternal_eligibility_post=instance)
                except:
                    raise CreateInfantEligibilityError(
                        'An ERROR occurred while attempting to create infant eligibility for {}'.format(instance)
                    )


@receiver(post_save, weak=False, dispatch_uid='update_registered_subject_from_consent_post_save')
def update_registered_subject_from_consent_post_save(sender, instance, raw, created, using, **kwargs):
    if not raw:
        if isinstance(instance, SubjectConsent):
            registered_subject = instance.maternal_eligibility_pre.registered_subject
            registered_subject.first_name = instance.first_name,
            registered_subject.last_name = instance.last_name,
            registered_subject.initials = instance.initials,
            registered_subject.gender = instance.gender,
            registered_subject.dob = instance.dob,
            registered_subject.identity = instance.identity,
            registered_subject.identity_type = instance.identity_type
            registered_subject.save()