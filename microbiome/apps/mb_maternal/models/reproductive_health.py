from django.db import models

from edc_base.model.fields import OtherCharField
from edc_base.audit_trail import AuditTrail
from edc_constants.choices import YES_NO_DWTA

from microbiome.apps.mb_list.models import Contraceptives, MaternalRelatives

from ..maternal_choices import (
    YES_NO_DNT_DWTA, NEXT_CHILD_PLAN, YES_NO_NO_PARTNER_DWTA, INFLUENTIAL_IN_DECISION_MAKING,
    PAP_SMEAR, NORMAL_ABNORMAL_DWTA, PAP_SMEAR_ESTIMATE)

from .maternal_crf_model import MaternalCrfModel


class ReproductiveHealth(MaternalCrfModel):

    """ A model completed by the user on the mother's sexual reproductive health. """

    more_children = models.CharField(
        verbose_name='Do you desire more children?',
        max_length=25,
        choices=YES_NO_DNT_DWTA,
        help_text='If the answer to this question is "YES" continue to '
                  'the next question else skip to question 5.')

    next_child = models.CharField(
        verbose_name='When would you like to have your next child?',
        max_length=35,
        choices=NEXT_CHILD_PLAN,
        blank=True,
        null=True,
        help_text='')

    contraceptive_measure = models.CharField(
        verbose_name='Have you discussed a contraceptive measure with a health care provider?',
        max_length=35,
        choices=YES_NO_DWTA,
        blank=True,
        null=True,
        help_text='')

    contraceptive_partner = models.CharField(
        verbose_name='Have you discussed a contraceptive method with your current partner?',
        max_length=10,
        choices=YES_NO_NO_PARTNER_DWTA,
        blank=True,
        null=True,
        help_text='')

    contraceptive_relative = models.ManyToManyField(
        MaternalRelatives,
        verbose_name='Have you discussed your contraceptive method with any of the following individuals? '
                     '(Please select all that apply)',
        blank=True,
        null=True,
        help_text='')

    contraceptive_relative_other = OtherCharField(
        max_length=35,
        verbose_name="If Other enter text description of other please give other people you discussed with",
        blank=True,
        null=True,
        help_text='If \'Other\' is selected above, please type in the person or persons '
                  '(by description only and not by name) with whom you have discussed your contraceptive method')

    influential_decision_making = models.CharField(
        verbose_name='Of the following individuals listed in questions 5-7, '
                     'please indicate who has influenced you the most in making the decision.',
        max_length=50,
        choices=INFLUENTIAL_IN_DECISION_MAKING,
        blank=True,
        null=True,
        help_text='')

    influential_decision_making_other = OtherCharField(
        max_length=35,
        verbose_name='If another person was most influential, please give details below.',
        blank=True,
        null=True)

    uses_contraceptive = models.CharField(
        verbose_name='Are you currently using a contraceptive method?',
        max_length=35,
        choices=YES_NO_DWTA,
        help_text='')

    contr = models.ManyToManyField(
        Contraceptives,
        verbose_name='Please share with us your current contraceptive methods',
        blank=True,
        null=True,
        help_text='')

    contr_other = OtherCharField(
        max_length=35,
        verbose_name="If Other enter text description of other contraceptive method being used",
        blank=True,
        null=True)

    pap_smear = models.CharField(
        verbose_name='Have you ever done pap smear?',
        max_length=35,
        choices=PAP_SMEAR,
        help_text='')

    pap_smear_date = models.DateField(
        verbose_name='Please provide the date of your last Pap smear.',
        blank=True,
        null=True,
        help_text='')

    pap_smear_estimate = models.CharField(
        verbose_name='Is the date of your last pap smear estimated?',
        max_length=60,
        choices=PAP_SMEAR_ESTIMATE,
        blank=True,
        null=True,
        help_text='If the exact date is not known, please indicate which part of the date is estimated.')

    pap_smear_result = models.CharField(
        verbose_name='Do you know the result of your last Pap smear',
        max_length=20,
        choices=YES_NO_DWTA,
        blank=True,
        null=True,
        help_text='')

    pap_smear_result_status = models.CharField(
        verbose_name='The results of my Pap smear were: ',
        max_length=30,
        choices=NORMAL_ABNORMAL_DWTA,
        blank=True,
        null=True,
        help_text='')

    pap_smear_result_abnormal = models.TextField(
        verbose_name='If the results of the Pap Smear were abnormal, can you please share the results with us: ',
        max_length=50,
        blank=True,
        null=True,
        help_text='')

    date_notified = models.DateField(
        verbose_name='When were you notified of these results?',
        blank=True,
        null=True,
        help_text=''
    )

    srh_referral = models.CharField(
        verbose_name='Would you like to be referred to the Sexual Reproductive Health Clinic?',
        max_length=25,
        choices=YES_NO_DWTA,
        help_text='')

    history = AuditTrail()

    class Meta:
        app_label = 'mb_maternal'
        verbose_name = 'Reproductive Health'
        verbose_name_plural = 'Reproductive Health'
