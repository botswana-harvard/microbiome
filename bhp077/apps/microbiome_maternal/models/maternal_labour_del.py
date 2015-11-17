from django.db import models
from django.db.models import get_model

from edc.core.identifier.classes import InfantIdentifier
from edc_base.audit_trail import AuditTrail
from edc_base.model.fields import OtherCharField
from edc_base.model.validators import datetime_not_future
from edc_constants.choices import YES_NO, YES_NO_UNKNOWN

from bhp077.apps.microbiome_list.models import Suppliments
from bhp077.apps.microbiome_list.models.maternal_lab_del import HealthCond, DelComp, ObComp
from bhp077.apps.microbiome_maternal.models import MaternalConsent, PostnatalEnrollment

from ..maternal_choices import DELIVERY_HEALTH_FACILITY
from .maternal_scheduled_visit_model import MaternalScheduledVisitModel


class MaternalLabourDel(MaternalScheduledVisitModel):

    """ Maternal Labor and Delivery which triggers registration of infants"""

    CONSENT_MODEL = MaternalConsent

    delivery_datetime = models.DateTimeField(
        verbose_name="Date and time of delivery :",
        help_text="If TIME unknown, estimate",
        validators=[
            datetime_not_future, ])

    del_time_is_est = models.CharField(
        verbose_name="Is the delivery TIME estimated?",
        max_length=3,
        choices=YES_NO,
        help_text="")

    labour_hrs = models.CharField(
        verbose_name="How long prior to to delivery, in HRS, did labour begin? ",
        max_length=10,
        help_text="")

    del_hosp = models.CharField(
        verbose_name="Where did the participant deliver? ",
        max_length=65,
        choices=DELIVERY_HEALTH_FACILITY,
        help_text="If 'OTHER', specify below",)
    del_hosp_other = OtherCharField()

    has_uterine_tender = models.CharField(
        max_length=10,
        choices=YES_NO_UNKNOWN,
        verbose_name="Was uterine tenderness recorded? ",
        help_text="")

    labr_max_temp = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        verbose_name="Indicate the maximum temperature of mother during labour",
        help_text="In degrees Celcius. -1 = unknown")

    has_chorioamnionitis = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name="Was chorio-amnionitis suspected? ",
        help_text="")

    has_del_comp = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name="Were there other complications at delivery? ",
        help_text="")

    live_infants_to_register = models.IntegerField(
        verbose_name="How many babies are you registering to the study? ",
        help_text="")

    del_comment = models.TextField(
        max_length=250,
        verbose_name="List any additional information about the labour and delivery (mother only) ",
        blank=True,
        null=True)

    comment = models.TextField(
        max_length=250,
        verbose_name="Comment if any additional pertinent information ",
        blank=True,
        null=True)

    history = AuditTrail()

    def post_save_create_infant_identifier(self, created):
        """Creates an identifier for registered infants"""
        maternal_consent = MaternalConsent.objects.get(registered_subject=self.maternal_visit.appointment.registered_subject)
        postnatal_enrol = PostnatalEnrollment.objects.get(registered_subject=maternal_consent.registered_subject)
        if created:
            if self.live_infants_to_register > 0:
                for infant_order in range(0, self.live_infants_to_register):
                    infant_identifier = InfantIdentifier(
                        maternal_identifier=self.maternal_visit.appointment.registered_subject.subject_identifier,
                        study_site=maternal_consent.study_site,
                        birth_order=infant_order,
                        live_infants=postnatal_enrol.live_infants,
                        live_infants_to_register=self.live_infants_to_register,
                        user=self.user_created)
                    infant_identifier.get_identifier()

    class Meta:
        app_label = 'microbiome_maternal'
        verbose_name = "Maternal Labour & Delivery"
        verbose_name_plural = "Maternal Labour & Delivery"


class MaternalLabDelMed(MaternalScheduledVisitModel):

    """ Medical history collected during labor and delivery. """

    CONSENT_MODEL = MaternalConsent

    has_health_cond = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name="Has the mother been newly diagnosed (during this pregnancy) "
        "with any major chronic health condition(s) that remain ongoing?",
        help_text="")

    health_cond = models.ManyToManyField(
        HealthCond,
        verbose_name="Select all that apply ",
        help_text="",
    )

    has_ob_comp = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name="During this pregnancy, did the mother have any of the following "
        "obstetrical complications?",
        help_text="")

    ob_comp = models.ManyToManyField(
        ObComp,
        verbose_name="Select all that apply",
        help_text="",
    )

    ob_comp_other = models.TextField(
        max_length=250,
        blank=True,
        null=True,
    )

    took_suppliments = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name="Did the mother take any of the following medications during this pregnancy?",
        help_text="")

    suppliments = models.ManyToManyField(
        Suppliments,
        verbose_name="Please select relevant medications taken:",
        help_text="Select all that apply")

    comment = models.TextField(
        max_length=250,
        verbose_name="Comment if any additional pertinent information ",
        blank=True,
        null=True)

    history = AuditTrail()

    class Meta:
        app_label = 'microbiome_maternal'
        verbose_name = "Maternal Labour & Delivery: Medical History"
        verbose_name_plural = "Maternal Labour & Delivery: Medical History"


class MaternalLabDelClinic(MaternalScheduledVisitModel):

    """ Laboratory and other clinical information collected during labor and delivery.
    for HIV +ve mothers ONLY"""

    CONSENT_MODEL = MaternalConsent

#     maternal_lab_del = models.OneToOneField(MaternalLabourDel)

    has_cd4 = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name=("During this pregnancy did the mother have at least one CD4 count"
                      " performed (outside the study)? "),
        help_text="")

    cd4_date = models.DateField(
        verbose_name="Date of most recent CD4 test? ",
        help_text="",
        blank=True,
        null=True)

    cd4_result = models.CharField(
        max_length=35,
        verbose_name="Result of most recent CD4 test",
        blank=True,
        null=True)

    has_vl = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name=("During this pregnancy did the mother have a viral load perfomed"
                      " (outside the study)? "),
        help_text="(if 'YES' continue. Otherwise go to question 9)")

    vl_date = models.DateField(
        verbose_name="If yes, Date of most recent VL test? ",
        help_text="",
        blank=True,
        null=True)

    vl_result = models.CharField(
        max_length=35,
        verbose_name="Result of most recent VL test",
        blank=True,
        null=True)

    comment = models.TextField(
        max_length=250,
        verbose_name="Comment if any additional pertinent information ",
        blank=True,
        null=True)

    history = AuditTrail()

    class Meta:
        app_label = 'microbiome_maternal'
        verbose_name = "Maternal LAB-DEL: Clinical History"
        verbose_name_plural = "Maternal LAB-DEL: Clinical History"


class MaternalLabDelDx(MaternalScheduledVisitModel):

    """ Diagnosis during pregnancy collected during labor and delivery.
    This is for HIV positive mothers only"""

    CONSENT_MODEL = MaternalConsent

    has_preg_dx = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name="During this pregnancy, did the mother have any of the following? ",
        help_text="If yes, Select all that apply in the table, only report grade 3 or 4 diagnoses")

    has_who_dx = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name="During this pregnancy, did the mother have any new diagnoses "
        "listed in the WHO Adult/Adolescent HIV clinical staging document which "
        "is/are NOT reported?",
        help_text="")

    history = AuditTrail()

    class Meta:
        app_label = 'microbiome_maternal'
        verbose_name = "Maternal LAB-DEL: Preg Dx"
        verbose_name_plural = "Maternal LAB-DEL: Preg Dx"


class MaternalLabDelDxT (MaternalScheduledVisitModel):

    """ Diagnosis during pregnancy collected during labor and delivery (transactions). """

    CONSENT_MODEL = MaternalConsent

    maternal_lab_del_dx = models.OneToOneField(MaternalLabDelDx)

    lab_del_dx = models.CharField(
        max_length=175,
        verbose_name="Diagnosis",
        help_text="")

    lab_del_dx_specify = models.CharField(
        max_length=50,
        verbose_name="Diagnosis specification",
        help_text="",
        blank=True,
        null=True)

    grade = models.IntegerField(
        verbose_name="Grade")

    hospitalized = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name="Hospitalized",
        help_text="")

    history = AuditTrail()

    def get_visit(self):
        return self.maternal_lab_del_dx.maternal_visit

    def get_report_datetime(self):
        return self.maternal_lab_del_dx.maternal_visit.report_datetime

    def get_subject_identifier(self):
        return self.maternal_lab_del_dx.maternal_visit.subject_identifier

    def __unicode__(self):
        return unicode(self.get_visit())

    class Meta:
        app_label = 'microbiome_maternal'
        verbose_name = "Maternal LAB-DEL: Preg DxT"
        verbose_name_plural = "Maternal LAB-DEL: Preg DxT"
