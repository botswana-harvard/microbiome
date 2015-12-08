from django.db.models.signals import post_save
from django.dispatch import receiver

from edc.core.identifier.classes import InfantIdentifier
from edc.subject.registration.models import RegisteredSubject

from .maternal_eligibility import MaternalEligibility
from .maternal_eligibility_loss import MaternalEligibilityLoss
from .maternal_visit import MaternalVisit
from .postnatal_enrollment import PostnatalEnrollment


@receiver(post_save, weak=False, dispatch_uid="maternal_eligibility_on_post_save")
def maternal_eligibility_on_post_save(sender, instance, raw, created, using, **kwargs):
    """Creates a MaternalEligibilityLoss instance if not eligible."""
    if not raw:
        if isinstance(instance, MaternalEligibility):
            if not instance.is_eligible:
                try:
                    maternal_eligibility_loss = MaternalEligibilityLoss.objects.get(
                        maternal_eligibility_id=instance.id)
                    maternal_eligibility_loss.report_datetime = instance.report_datetime
                    maternal_eligibility_loss.reason_ineligible = instance.ineligibility
                    maternal_eligibility_loss.user_modified = instance.user_modified
                    maternal_eligibility_loss.save()
                except MaternalEligibilityLoss.DoesNotExist:
                    MaternalEligibilityLoss.objects.create(
                        maternal_eligibility_id=instance.id,
                        report_datetime=instance.report_datetime,
                        reason_ineligible=instance.ineligibility,
                        user_created=instance.user_created,
                        user_modified=instance.user_modified)
            else:
                MaternalEligibilityLoss.objects.filter(maternal_eligibility_id=instance.id).delete()


@receiver(post_save, weak=False, dispatch_uid="criteria_passed_create_registered_subject")
def criteria_passed_create_registered_subject(sender, instance, raw, created, using, **kwargs):
    """Creates a Registered Subject ONLY if maternal eligibility is passed."""
    if not raw:
        if isinstance(instance, MaternalEligibility):
            if instance.is_eligible:
                if not instance.registered_subject:
                    registered_subject = RegisteredSubject.objects.create(
                        created=instance.created,
                        first_name='Mother',
                        gender='F',
                        subject_type='maternal',
                        registration_datetime=instance.created,
                        user_created=instance.user_created)
                    instance.registered_subject = registered_subject
                    instance.save()


@receiver(post_save, weak=False, dispatch_uid="maternal_consent_on_post_save")
def maternal_consent_on_post_save(sender, instance, raw, created, using, **kwargs):
    """This will update the is_consented boolean on maternal eligibility"""
    if not raw:
        try:
            instance.update_is_consented()
        except AttributeError as e:
            if 'update_is_consented' not in str(e):
                raise AttributeError(str(e))


@receiver(post_save, weak=False, dispatch_uid='update_registered_subject_on_post_save')
def update_registered_subject_on_post_save(sender, instance, raw, created, using, **kwargs):
    """Updates an instance of RegisteredSubject from the Maternal Consent"""
    if not raw:
        try:
            instance.registered_subject.last_name = instance.last_name
            instance.registered_subject.dob = instance.dob
            instance.registered_subject.first_name = instance.first_name
            instance.registered_subject.gender = instance.gender
            instance.registered_subject.identity = instance.identity
            instance.registered_subject.identity_type = instance.identity_type
            instance.registered_subject.initials = instance.initials
            instance.registered_subject.is_dob_estimated = instance.is_dob_estimated
            instance.registered_subject.study_site = instance.study_site
            instance.registered_subject.subject_identifier = instance.subject_identifier
            instance.registered_subject.save(using=using)
        except AttributeError as e:
            if 'registered_subject' not in str(e) and 'last_name' not in str(e):
                raise AttributeError(str(e))


@receiver(post_save, weak=False, dispatch_uid="maternal_visit_on_post_save")
def maternal_visit_on_post_save(sender, instance, raw, created, using, **kwargs):
    """Updates maternal scheduled meta data."""
    if not raw:
        if isinstance(instance, MaternalVisit):
            instance.maternal_offstudy_required()
            instance.maternal_death_required()
            instance.update_maternal_scheduled_entry_meta_data()
            instance.update_entry_meta_data()


@receiver(post_save, weak=False, dispatch_uid="save_common_fields_to_postnatal_enrollment_post_save")
def save_common_fields_to_postnatal_enrollment_post_save(sender, instance, raw, created, using, **kwargs):
    """Updates common fields on postnatal_enrollment with values from antenatal_enrollment."""
    if not raw:
        try:
            instance.save_common_fields_to_postnatal_enrollment()
        except AttributeError as e:
            if 'save_common_fields_to_postnatal_enrollment' not in str(e):
                raise AttributeError(str(e))


@receiver(post_save, weak=False, dispatch_uid='create_infant_identifier_on_labour_delivery')
def create_infant_identifier_on_labour_delivery(sender, instance, raw, created, using, **kwargs):
    """Creates an identifier for registered infants"""
    if not raw and created:
        try:
            if instance.live_infants_to_register > 0:
                registered_subject = instance.maternal_visit.appointment.registered_subject
                consent = instance.CONSENT_MODEL.objects.get(
                    registered_subject=registered_subject)
                postnatal_enrollment = PostnatalEnrollment.objects.get(
                    registered_subject=consent.registered_subject)
                for infant_order in range(0, instance.live_infants_to_register):
                    infant_identifier = InfantIdentifier(
                        maternal_identifier=registered_subject.subject_identifier,
                        study_site=consent.study_site,
                        birth_order=infant_order,
                        live_infants=postnatal_enrollment.live_infants,
                        live_infants_to_register=instance.live_infants_to_register,
                        user=instance.user_created)
                    infant_identifier.get_identifier()
        except AttributeError:
            pass
