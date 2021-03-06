from django.test.testcases import TestCase

from edc_constants.constants import POS, YES
from edc_registration.models import RegisteredSubject
from edc_appointment.models import Appointment

from microbiome.apps.mb.constants import INFANT
from microbiome.load_edc import load_edc

from microbiome.apps.mb_maternal.tests.factories import (
    MaternalEligibilityFactory, MaternalConsentFactory, PostnatalEnrollmentFactory,
    MaternalLabourDelFactory, MaternalVisitFactory)

from microbiome.apps.mb_infant.tests.factories import (
    InfantBirthFactory, InfantVisitFactory, InfantCleftDisorderFactory,
    InfantCongenitalAnomaliesFactory, InfantFuImmunizationsFactory, InfantCardioDisorderFactory,
    InfantBirthFeedVaccineFactory, InfantFuDxFactory, InfantFuDxItemsFactory, InfantArvProphFactory,
    InfantArvProphModFactory, InfantVaccinesFactory, VaccinesReceivedFactory, VaccinesMissedFactory,
    InfantFuNewMedFactory, InfantFuNewMedItemsFactory)


class BaseTestCase(TestCase):

    def setUp(self):
        load_edc()

    def infant_instances(self):
        instances = []
        maternal_eligibility = MaternalEligibilityFactory()
        instances.append(maternal_eligibility)
        maternal_consent = MaternalConsentFactory(
            registered_subject=maternal_eligibility.registered_subject)
        instances.append(maternal_consent)
        maternal_registered_subject = maternal_consent.registered_subject
        instances.append(maternal_registered_subject)
        post_natal_enrollment = PostnatalEnrollmentFactory(
            registered_subject=maternal_registered_subject,
            current_hiv_status=POS,
            evidence_hiv_status=YES)
        instances.append(post_natal_enrollment)
        maternal_appointment_1000 = Appointment.objects.get(registered_subject=maternal_registered_subject,
                                                            visit_definition__code='1000M')
        instances.append(maternal_appointment_1000)
        maternal_visit_1000 = MaternalVisitFactory(appointment=maternal_appointment_1000)
        instances.append(maternal_visit_1000)

        maternal_appointment_2000 = Appointment.objects.get(registered_subject=maternal_registered_subject,
                                                            visit_definition__code='2000M')
        instances.append(maternal_appointment_2000)
        maternal_visit_2000 = MaternalVisitFactory(appointment=maternal_appointment_2000)
        instances.append(maternal_visit_2000)

        maternal_labour_del = MaternalLabourDelFactory(maternal_visit=maternal_visit_2000)
        instances.append(maternal_labour_del)
        infant_registered_subject = RegisteredSubject.objects.get(
            relative_identifier=maternal_registered_subject.subject_identifier,
            subject_type=INFANT)
        instances.append(infant_registered_subject)
        infant_birth = InfantBirthFactory(
            registered_subject=infant_registered_subject,
            maternal_labour_del=maternal_labour_del)
        instances.append(infant_birth)
        infant_appointment_2000 = Appointment.objects.get(
            registered_subject=infant_registered_subject,
            visit_definition__code='2000')
        instances.append(infant_appointment_2000)
        infant_visit_2000 = InfantVisitFactory(appointment=infant_appointment_2000)
        instances.append(infant_visit_2000)
        infant_congenital_anomalies = InfantCongenitalAnomaliesFactory(infant_visit=infant_visit_2000)
        instances.append(infant_congenital_anomalies)
        cardio_disorder = InfantCardioDisorderFactory(congenital_anomalies=infant_congenital_anomalies)
        instances.append(cardio_disorder)
        cleft_disorder = InfantCleftDisorderFactory(congenital_anomalies=infant_congenital_anomalies)
        instances.append(cleft_disorder)
        infant_birth_feed_vaccine = InfantBirthFeedVaccineFactory(infant_visit=infant_visit_2000)
        instances.append(infant_birth_feed_vaccine)
        infant_vaccines = InfantVaccinesFactory(infant_birth_feed_vaccine=infant_birth_feed_vaccine)
        instances.append(infant_vaccines)
        infant_appointment_2010 = Appointment.objects.get(
            registered_subject=infant_registered_subject,
            visit_definition__code='2010')
        instances.append(infant_appointment_2010)
        infant_visit_2010 = InfantVisitFactory(appointment=infant_appointment_2010)
        infant_fu_immuninization = InfantFuImmunizationsFactory(infant_visit=infant_visit_2010)
        instances.append(infant_fu_immuninization)
        infant_fu_new_med = InfantFuNewMedFactory(infant_visit=infant_visit_2010)
        instances.append(infant_fu_new_med)
        infant_fu_new_med_items = InfantFuNewMedItemsFactory(infant_fu_med=infant_fu_new_med)
        instances.append(infant_fu_new_med_items)
        vaccines_received = VaccinesReceivedFactory(infant_fu_immunizations=infant_fu_immuninization)
        instances.append(vaccines_received)
        vaccines_missed = VaccinesMissedFactory(infant_fu_immunizations=infant_fu_immuninization)
        instances.append(vaccines_missed)
        infant_fu_dx = InfantFuDxFactory(infant_visit=infant_visit_2010)
        instances.append(infant_fu_dx)
        infant_fu_dx_items = InfantFuDxItemsFactory(infant_fu_dx=infant_fu_dx)
        instances.append(infant_fu_dx_items)
        infant_arv_proph = InfantArvProphFactory(infant_visit=infant_visit_2010)
        instances.append(infant_arv_proph)
        infant_arv_proph_mod = InfantArvProphModFactory(infant_arv_proph=infant_arv_proph)
        instances.append(infant_arv_proph_mod)
        return instances
