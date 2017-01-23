from collections import OrderedDict

from edc_constants.constants import REQUIRED, NOT_REQUIRED, ADDITIONAL, NOT_ADDITIONAL
from edc_visit_schedule.classes import (
    VisitScheduleConfiguration, site_visit_schedules,
    CrfTuple, MembershipFormTuple, ScheduleTuple, RequisitionPanelTuple)

from microbiome.apps.mb.constants import INFANT

from ..models import InfantVisit, InfantBirth


class InfantBirthVisitSchedule(VisitScheduleConfiguration):

    name = 'birth visit schedule'
    app_label = 'mb_infant'

    membership_forms = OrderedDict({
        'infant_enrollment': MembershipFormTuple('infant_enrollment', InfantBirth, True)})

    schedules = OrderedDict({
        'Infant Enrollment': ScheduleTuple('Infant Enrollment',
                                           'infant_enrollment', None, None)})
    visit_definitions = OrderedDict()
    visit_definitions['2000'] = {
        'title': 'Birth',
        'time_point': 0,
        'base_interval': 0,
        'base_interval_unit': 'D',
        'window_lower_bound': 0,
        'window_lower_bound_unit': 'D',
        'window_upper_bound': 0,
        'window_upper_bound_unit': 'D',
        'grouping': INFANT,
        'visit_tracking_model': InfantVisit,
        'schedule': 'Infant Enrollment',
        'instructions': None,
        'requisitions': (
            RequisitionPanelTuple(10L, u'mb_lab', u'infantrequisition',
                                  'DNA PCR', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
            RequisitionPanelTuple(20L, u'mb_lab', u'infantrequisition',
                                  'Stool storage', 'STORAGE', 'ST', NOT_REQUIRED, ADDITIONAL),
            RequisitionPanelTuple(30L, u'mb_lab', u'infantrequisition',
                                  'PBMC Plasma (STORE ONLY)', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
            RequisitionPanelTuple(40L, u'mb_lab', u'infantrequisition',
                                  'Rectal swab (Storage)', 'STORAGE', 'RS', REQUIRED, NOT_ADDITIONAL),
            RequisitionPanelTuple(70L, u'mb_lab', u'infantrequisition',
                                  'Viral Load', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
            RequisitionPanelTuple(80L, u'mb_lab', u'infantrequisition',
                                  'Chemistry', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
            RequisitionPanelTuple(90L, u'mb_lab', u'infantrequisition',
                                  'Hematology (ARV)', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
        ),
        'entries': (
            CrfTuple(10L, u'mb_infant', u'infantbirthdata', REQUIRED, NOT_ADDITIONAL),
            CrfTuple(20L, u'mb_infant', u'infantbirthexam', REQUIRED, NOT_ADDITIONAL),
            CrfTuple(30L, u'mb_infant', u'infantbirthfeedvaccine', REQUIRED, NOT_ADDITIONAL),
            CrfTuple(40L, u'mb_infant', u'infantbirtharv', NOT_REQUIRED, ADDITIONAL),
            CrfTuple(50L, u'mb_infant', u'infantstoolcollection', REQUIRED, NOT_ADDITIONAL),
            CrfTuple(100L, u'mb_infant', u'infantcongenitalanomalies', NOT_REQUIRED, ADDITIONAL),
            CrfTuple(200L, u'mb_infant', u'infantdeathreport', NOT_REQUIRED, ADDITIONAL),
            CrfTuple(230L, u'mb_infant', u'infantoffstudy', NOT_REQUIRED, ADDITIONAL))}
    visit_definitions['2010'] = {
        'title': 'Infant 1 Month Visit',
        'time_point': 10,
        'base_interval': 27,
        'base_interval_unit': 'D',
        'window_lower_bound': 0,
        'window_lower_bound_unit': 'D',
        'window_upper_bound': 0,
        'window_upper_bound_unit': 'D',
        'grouping': INFANT,
        'visit_tracking_model': InfantVisit,
        'schedule': 'Infant Enrollment',
        'instructions': None,
        'requisitions': (
            RequisitionPanelTuple(10L, u'mb_lab', u'infantrequisition',
                                  'DNA PCR', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
            RequisitionPanelTuple(20L, u'mb_lab', u'infantrequisition',
                                  'Stool storage', 'STORAGE', 'ST', NOT_REQUIRED, ADDITIONAL),
            RequisitionPanelTuple(30L, u'mb_lab', u'infantrequisition',
                                  'PBMC Plasma (STORE ONLY)', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
            RequisitionPanelTuple(40L, u'mb_lab', u'infantrequisition',
                                  'Rectal swab (Storage)', 'STORAGE', 'RS', REQUIRED, NOT_ADDITIONAL),
            RequisitionPanelTuple(70L, u'mb_lab', u'infantrequisition',
                                  'Viral Load', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
            RequisitionPanelTuple(80L, u'mb_lab', u'infantrequisition',
                                  'Chemistry', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
            RequisitionPanelTuple(90L, u'mb_lab', u'infantrequisition',
                                  'Hematology (ARV)', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
        ),
        'entries': (
            CrfTuple(30L, u'mb_infant', u'infantfu', REQUIRED, NOT_ADDITIONAL),
            CrfTuple(40L, u'mb_infant', u'infantfuphysical', REQUIRED, NOT_ADDITIONAL),
            CrfTuple(50L, u'mb_infant', u'infantfudx', NOT_REQUIRED, ADDITIONAL),
            CrfTuple(80L, u'mb_infant', u'infantfunewmed', REQUIRED, NOT_ADDITIONAL),
            CrfTuple(80L, u'mb_infant', u'infantfuimmunizations', REQUIRED, NOT_ADDITIONAL),
            CrfTuple(90L, u'mb_infant', u'infantarvproph', REQUIRED, ADDITIONAL),
            CrfTuple(100L, u'mb_infant', u'infantfeeding', REQUIRED, NOT_ADDITIONAL),
            CrfTuple(110L, u'mb_infant', u'infantstoolcollection', REQUIRED, NOT_ADDITIONAL),
            CrfTuple(200L, u'mb_infant', u'infantdeathreport', NOT_REQUIRED, ADDITIONAL),
            CrfTuple(240L, u'mb_infant', u'infantoffstudy', NOT_REQUIRED, ADDITIONAL))}
    visit_definitions['2030'] = {
        'title': 'Infant 3 Month Visit',
        'time_point': 30,
        'base_interval': 3,
        'base_interval_unit': 'M',
        'window_lower_bound': 0,
        'window_lower_bound_unit': 'D',
        'window_upper_bound': 0,
        'window_upper_bound_unit': 'D',
        'grouping': INFANT,
        'visit_tracking_model': InfantVisit,
        'schedule': 'Infant Enrollment',
        'instructions': None,
        'requisitions': (
            RequisitionPanelTuple(10L, u'mb_lab', u'infantrequisition',
                                  'DNA PCR', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
            RequisitionPanelTuple(20L, u'mb_lab', u'infantrequisition',
                                  'Stool storage', 'STORAGE', 'ST', NOT_REQUIRED, ADDITIONAL),
            RequisitionPanelTuple(30L, u'mb_lab', u'infantrequisition',
                                  'PBMC Plasma (STORE ONLY)', 'STORAGE', 'WB', REQUIRED, NOT_ADDITIONAL),
            RequisitionPanelTuple(40L, u'mb_lab', u'infantrequisition',
                                  'Rectal swab (Storage)', 'STORAGE', 'RS', REQUIRED, NOT_ADDITIONAL),
            RequisitionPanelTuple(60L, u'mb_lab', u'infantrequisition',
                                  'Inflammatory Cytokines', 'STORAGE', 'WB', REQUIRED, NOT_ADDITIONAL),
            RequisitionPanelTuple(70L, u'mb_lab', u'infantrequisition',
                                  'Viral Load', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
            RequisitionPanelTuple(80L, u'mb_lab', u'infantrequisition',
                                  'Chemistry', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
            RequisitionPanelTuple(90L, u'mb_lab', u'infantrequisition',
                                  'Hematology (ARV)', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
        ),
        'entries': (
            CrfTuple(30L, u'mb_infant', u'infantfu', REQUIRED, NOT_ADDITIONAL),
            CrfTuple(40L, u'mb_infant', u'infantfuphysical', REQUIRED, NOT_ADDITIONAL),
            CrfTuple(50L, u'mb_infant', u'infantfudx', NOT_REQUIRED, ADDITIONAL),
            CrfTuple(80L, u'mb_infant', u'infantfunewmed', REQUIRED, NOT_ADDITIONAL),
            CrfTuple(80L, u'mb_infant', u'infantfuimmunizations', REQUIRED, NOT_ADDITIONAL),
            CrfTuple(90L, u'mb_infant', u'infantarvproph', REQUIRED, ADDITIONAL),
            CrfTuple(100L, u'mb_infant', u'infantfeeding', REQUIRED, NOT_ADDITIONAL),
            CrfTuple(110L, u'mb_infant', u'infantstoolcollection', REQUIRED, NOT_ADDITIONAL),
            CrfTuple(110L, u'mb_infant', u'infantcircumcision', NOT_REQUIRED, ADDITIONAL),
            CrfTuple(200L, u'mb_infant', u'infantdeathreport', NOT_REQUIRED, ADDITIONAL),
            CrfTuple(240L, u'mb_infant', u'infantoffstudy', NOT_REQUIRED, ADDITIONAL))}

    visit_definitions['2060'] = {
        'title': 'Infant 6 Month Visit',
        'time_point': 60,
        'base_interval': 6,
        'base_interval_unit': 'M',
        'window_lower_bound': 0,
        'window_lower_bound_unit': 'D',
        'window_upper_bound': 0,
        'window_upper_bound_unit': 'D',
        'grouping': INFANT,
        'visit_tracking_model': InfantVisit,
        'schedule': 'Infant Enrollment',
        'instructions': None,
        'requisitions': (
            RequisitionPanelTuple(10L, u'mb_lab', u'infantrequisition',
                                  'DNA PCR', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
            RequisitionPanelTuple(20L, u'mb_lab', u'infantrequisition',
                                  'Stool storage', 'STORAGE', 'ST', NOT_REQUIRED, ADDITIONAL),
            RequisitionPanelTuple(30L, u'mb_lab', u'infantrequisition',
                                  'PBMC Plasma (STORE ONLY)', 'STORAGE', 'WB', REQUIRED, NOT_ADDITIONAL),
            RequisitionPanelTuple(40L, u'mb_lab', u'infantrequisition',
                                  'Rectal swab (Storage)', 'STORAGE', 'RS', REQUIRED, NOT_ADDITIONAL),
            RequisitionPanelTuple(60L, u'mb_lab', u'infantrequisition',
                                  'Inflammatory Cytokines', 'STORAGE', 'WB', REQUIRED, NOT_ADDITIONAL),
            RequisitionPanelTuple(70L, u'mb_lab', u'infantrequisition',
                                  'Viral Load', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
            RequisitionPanelTuple(80L, u'mb_lab', u'infantrequisition',
                                  'Chemistry', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
            RequisitionPanelTuple(90L, u'mb_lab', u'infantrequisition',
                                  'Hematology (ARV)', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
        ),
        'entries': (
            CrfTuple(30L, u'mb_infant', u'infantfu', REQUIRED, NOT_ADDITIONAL),
            CrfTuple(40L, u'mb_infant', u'infantfuphysical', REQUIRED, NOT_ADDITIONAL),
            CrfTuple(50L, u'mb_infant', u'infantfudx', NOT_REQUIRED, ADDITIONAL),
            CrfTuple(80L, u'mb_infant', u'infantfunewmed', REQUIRED, NOT_ADDITIONAL),
            CrfTuple(80L, u'mb_infant', u'infantfuimmunizations', REQUIRED, NOT_ADDITIONAL),
            CrfTuple(90L, u'mb_infant', u'infantarvproph', REQUIRED, ADDITIONAL),
            CrfTuple(100L, u'mb_infant', u'infantfeeding', REQUIRED, NOT_ADDITIONAL),
            CrfTuple(110L, u'mb_infant', u'infantstoolcollection', REQUIRED, NOT_ADDITIONAL),
            CrfTuple(110L, u'mb_infant', u'infantcircumcision', NOT_REQUIRED, ADDITIONAL),
            CrfTuple(200L, u'mb_infant', u'infantdeathreport', NOT_REQUIRED, ADDITIONAL),
            CrfTuple(240L, u'mb_infant', u'infantoffstudy', NOT_REQUIRED, ADDITIONAL))}

    visit_definitions['2090'] = {
        'title': 'Infant 9 Month Visit',
        'time_point': 90,
        'base_interval': 9,
        'base_interval_unit': 'M',
        'window_lower_bound': 0,
        'window_lower_bound_unit': 'D',
        'window_upper_bound': 0,
        'window_upper_bound_unit': 'D',
        'grouping': INFANT,
        'visit_tracking_model': InfantVisit,
        'schedule': 'Infant Enrollment',
        'instructions': None,
        'requisitions': (
            RequisitionPanelTuple(10L, u'mb_lab', u'infantrequisition',
                                  'DNA PCR', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
            RequisitionPanelTuple(20L, u'mb_lab', u'infantrequisition',
                                  'Stool storage', 'STORAGE', 'ST', NOT_REQUIRED, ADDITIONAL),
            RequisitionPanelTuple(30L, u'mb_lab', u'infantrequisition',
                                  'PBMC Plasma (STORE ONLY)', 'STORAGE', 'WB', REQUIRED, NOT_ADDITIONAL),
            RequisitionPanelTuple(40L, u'mb_lab', u'infantrequisition',
                                  'Rectal swab (Storage)', 'STORAGE', 'RS', REQUIRED, NOT_ADDITIONAL),
            RequisitionPanelTuple(60L, u'mb_lab', u'infantrequisition',
                                  'Inflammatory Cytokines', 'STORAGE', 'WB', REQUIRED, NOT_ADDITIONAL),
            RequisitionPanelTuple(70L, u'mb_lab', u'infantrequisition',
                                  'Viral Load', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
            RequisitionPanelTuple(80L, u'mb_lab', u'infantrequisition',
                                  'Chemistry', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
            RequisitionPanelTuple(90L, u'mb_lab', u'infantrequisition',
                                  'Hematology (ARV)', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
        ),
        'entries': (
            CrfTuple(30L, u'mb_infant', u'infantfu', REQUIRED, NOT_ADDITIONAL),
            CrfTuple(40L, u'mb_infant', u'infantfuphysical', REQUIRED, NOT_ADDITIONAL),
            CrfTuple(50L, u'mb_infant', u'infantfudx', NOT_REQUIRED, ADDITIONAL),
            CrfTuple(80L, u'mb_infant', u'infantfunewmed', REQUIRED, NOT_ADDITIONAL),
            CrfTuple(80L, u'mb_infant', u'infantfuimmunizations', REQUIRED, NOT_ADDITIONAL),
            CrfTuple(90L, u'mb_infant', u'infantarvproph', REQUIRED, ADDITIONAL),
            CrfTuple(100L, u'mb_infant', u'infantfeeding', REQUIRED, NOT_ADDITIONAL),
            CrfTuple(110L, u'mb_infant', u'infantstoolcollection', REQUIRED, NOT_ADDITIONAL),
            CrfTuple(200L, u'mb_infant', u'infantdeathreport', NOT_REQUIRED, ADDITIONAL),
            CrfTuple(240L, u'mb_infant', u'infantoffstudy', NOT_REQUIRED, ADDITIONAL))}

    visit_definitions['2120'] = {
        'title': 'Infant 12 Month Visit',
        'time_point': 120,
        'base_interval': 12,
        'base_interval_unit': 'M',
        'window_lower_bound': 0,
        'window_lower_bound_unit': 'D',
        'window_upper_bound': 0,
        'window_upper_bound_unit': 'D',
        'grouping': INFANT,
        'visit_tracking_model': InfantVisit,
        'schedule': 'Infant Enrollment',
        'instructions': None,
        'requisitions': (
            RequisitionPanelTuple(10L, u'mb_lab', u'infantrequisition',
                                  'DNA PCR', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
            RequisitionPanelTuple(20L, u'mb_lab', u'infantrequisition',
                                  'Stool storage', 'STORAGE', 'ST', NOT_REQUIRED, ADDITIONAL),
            RequisitionPanelTuple(30L, u'mb_lab', u'infantrequisition',
                                  'PBMC Plasma (STORE ONLY)', 'STORAGE', 'WB', NOT_REQUIRED, NOT_ADDITIONAL),
            RequisitionPanelTuple(40L, u'mb_lab', u'infantrequisition',
                                  'Rectal swab (Storage)', 'STORAGE', 'RS', REQUIRED, NOT_ADDITIONAL),
            RequisitionPanelTuple(70L, u'mb_lab', u'infantrequisition',
                                  'Viral Load', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
            RequisitionPanelTuple(80L, u'mb_lab', u'infantrequisition',
                                  'Chemistry', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
            RequisitionPanelTuple(90L, u'mb_lab', u'infantrequisition',
                                  'Hematology (ARV)', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
        ),
        'entries': (
            CrfTuple(30L, u'mb_infant', u'infantfu', REQUIRED, NOT_ADDITIONAL),
            CrfTuple(40L, u'mb_infant', u'infantfuphysical', REQUIRED, NOT_ADDITIONAL),
            CrfTuple(50L, u'mb_infant', u'infantfudx', NOT_REQUIRED, ADDITIONAL),
            CrfTuple(80L, u'mb_infant', u'infantfunewmed', REQUIRED, NOT_ADDITIONAL),
            CrfTuple(80L, u'mb_infant', u'infantfuimmunizations', REQUIRED, NOT_ADDITIONAL),
            CrfTuple(90L, u'mb_infant', u'infantarvproph', REQUIRED, ADDITIONAL),
            CrfTuple(100L, u'mb_infant', u'infantfeeding', REQUIRED, NOT_ADDITIONAL),
            CrfTuple(110L, u'mb_infant', u'infantstoolcollection', REQUIRED, NOT_ADDITIONAL),
            CrfTuple(200L, u'mb_infant', u'infantdeathreport', NOT_REQUIRED, ADDITIONAL),
            CrfTuple(240L, u'mb_infant', u'infantoffstudy', REQUIRED, ADDITIONAL))}

site_visit_schedules.register(InfantBirthVisitSchedule)
