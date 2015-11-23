from collections import OrderedDict

from edc.subject.visit_schedule.classes import (VisitScheduleConfiguration, site_visit_schedules,
                                                EntryTuple, MembershipFormTuple, ScheduleGroupTuple,
                                                RequisitionPanelTuple)
from edc_constants.constants import REQUIRED, NOT_REQUIRED, ADDITIONAL, NOT_ADDITIONAL

from ..models import InfantVisit, InfantBirth


class InfantBirthVisitSchedule(VisitScheduleConfiguration):

    name = 'birth visit schedule'
    app_label = 'microbiome_infant'

    membership_forms = OrderedDict({
        'infant_enrollment': MembershipFormTuple('infant_enrollment', InfantBirth, True)})

    schedule_groups = OrderedDict({
        'Infant Enrollment': ScheduleGroupTuple('Infant Enrollment',
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
        'grouping': 'infant',
        'visit_tracking_model': InfantVisit,
        'schedule_group': 'Infant Enrollment',
        'instructions': None,
        'requisitions': (
            RequisitionPanelTuple(300L, u'microbiome_lab', u'infantrequisition',
                                  'DNA PCR', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
            RequisitionPanelTuple(400L, u'microbiome_lab', u'infantrequisition',
                                  'Stool storage', 'STORAGE', 'ST', REQUIRED, NOT_ADDITIONAL),
            RequisitionPanelTuple(500L, u'microbiome_lab', u'infantrequisition',
                                  'Rectal swab (Storage)', 'STORAGE', 'RS', REQUIRED, NOT_ADDITIONAL)),
        'entries': (
            EntryTuple(10L, u'microbiome_infant', u'infantbirthdata', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(20L, u'microbiome_infant', u'infantbirthexam', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(30L, u'microbiome_infant', u'infantbirthfeedvaccine', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(40L, u'microbiome_infant', u'infantbirtharv', NOT_REQUIRED, ADDITIONAL),
            EntryTuple(50L, u'microbiome_infant', u'infantstoolcollection', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(100L, u'microbiome_infant', u'infantcongenitalanomalies', NOT_REQUIRED, ADDITIONAL),
            EntryTuple(200L, u'microbiome_infant', u'infantdeath', NOT_REQUIRED, ADDITIONAL),
            EntryTuple(230L, u'microbiome_infant', u'infantoffstudy', NOT_REQUIRED, ADDITIONAL))}
    visit_definitions['2010'] = {
        'title': 'Infant 1 Month Visit',
        'time_point': 10,
        'base_interval': 27,
        'base_interval_unit': 'D',
        'window_lower_bound': 0,
        'window_lower_bound_unit': 'D',
        'window_upper_bound': 0,
        'window_upper_bound_unit': 'D',
        'grouping': 'infant',
        'visit_tracking_model': InfantVisit,
        'schedule_group': 'Infant Enrollment',
        'instructions': None,
        'requisitions': (
            RequisitionPanelTuple(300L, u'microbiome_lab', u'infantrequisition',
                                  'DNA PCR', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
            RequisitionPanelTuple(400L, u'microbiome_lab', u'infantrequisition',
                                  'Stool storage', 'STORAGE', 'ST', REQUIRED, NOT_ADDITIONAL),
            RequisitionPanelTuple(500L, u'microbiome_lab', u'infantrequisition',
                                  'Rectal swab (Storage)', 'STORAGE', 'RS', REQUIRED, NOT_ADDITIONAL)),
        'entries': (
            EntryTuple(30L, u'microbiome_infant', u'infantfu', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(40L, u'microbiome_infant', u'infantfuphysical', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(50L, u'microbiome_infant', u'infantfudx', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(80L, u'microbiome_infant', u'infantfunewmed', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(80L, u'microbiome_infant', u'infantfuimmunizations', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(90L, u'microbiome_infant', u'infantarvproph', NOT_REQUIRED, ADDITIONAL),
            EntryTuple(100L, u'microbiome_infant', u'infantfeeding', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(110L, u'microbiome_infant', u'infantstoolcollection', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(200L, u'microbiome_infant', u'infantdeath', NOT_REQUIRED, ADDITIONAL),
            EntryTuple(240L, u'microbiome_infant', u'infantoffstudy', NOT_REQUIRED, ADDITIONAL))}
    visit_definitions['2030'] = {
        'title': 'Infant 3 Month Visit',
        'time_point': 30,
        'base_interval': 27,
        'base_interval_unit': 'D',
        'window_lower_bound': 0,
        'window_lower_bound_unit': 'D',
        'window_upper_bound': 0,
        'window_upper_bound_unit': 'D',
        'grouping': 'infant',
        'visit_tracking_model': InfantVisit,
        'schedule_group': 'Infant Enrollment',
        'instructions': None,
        'requisitions': (
            RequisitionPanelTuple(300L, u'microbiome_lab', u'infantrequisition',
                                  'DNA PCR', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
            RequisitionPanelTuple(400L, u'microbiome_lab', u'infantrequisition',
                                  'Stool storage', 'STORAGE', 'ST', REQUIRED, NOT_ADDITIONAL),
            RequisitionPanelTuple(500L, u'microbiome_lab', u'infantrequisition',
                                  'Rectal swab (Storage)', 'STORAGE', 'RS', REQUIRED, NOT_ADDITIONAL)),
        'entries': (
            EntryTuple(30L, u'microbiome_infant', u'infantfu', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(40L, u'microbiome_infant', u'infantfuphysical', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(50L, u'microbiome_infant', u'infantfudx', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(80L, u'microbiome_infant', u'infantfunewmed', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(80L, u'microbiome_infant', u'infantfuimmunizations', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(90L, u'microbiome_infant', u'infantarvproph', NOT_REQUIRED, ADDITIONAL),
            EntryTuple(100L, u'microbiome_infant', u'infantfeeding', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(110L, u'microbiome_infant', u'infantstoolcollection', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(110L, u'microbiome_infant', u'infantcircumcision', NOT_REQUIRED, ADDITIONAL),
            EntryTuple(200L, u'microbiome_infant', u'infantdeath', NOT_REQUIRED, ADDITIONAL),
            EntryTuple(240L, u'microbiome_infant', u'infantoffstudy', NOT_REQUIRED, ADDITIONAL))}

    visit_definitions['2060'] = {
        'title': 'Infant 6 Month Visit',
        'time_point': 60,
        'base_interval': 0,
        'base_interval_unit': 'M',
        'window_lower_bound': 0,
        'window_lower_bound_unit': 'D',
        'window_upper_bound': 0,
        'window_upper_bound_unit': 'D',
        'grouping': 'infant',
        'visit_tracking_model': InfantVisit,
        'schedule_group': 'Infant Enrollment',
        'instructions': None,
        'requisitions': (
            RequisitionPanelTuple(300L, u'microbiome_lab', u'infantrequisition',
                                  'DNA PCR', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
            RequisitionPanelTuple(400L, u'microbiome_lab', u'infantrequisition',
                                  'Stool storage', 'STORAGE', 'ST', REQUIRED, NOT_ADDITIONAL),
            RequisitionPanelTuple(500L, u'microbiome_lab', u'infantrequisition',
                                  'Rectal swab (Storage)', 'STORAGE', 'RS', REQUIRED, NOT_ADDITIONAL)),
        'entries': (
            EntryTuple(30L, u'microbiome_infant', u'infantfu', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(40L, u'microbiome_infant', u'infantfuphysical', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(50L, u'microbiome_infant', u'infantfudx', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(80L, u'microbiome_infant', u'infantfunewmed', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(80L, u'microbiome_infant', u'infantfuimmunizations', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(90L, u'microbiome_infant', u'infantarvproph', NOT_REQUIRED, ADDITIONAL),
            EntryTuple(100L, u'microbiome_infant', u'infantfeeding', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(110L, u'microbiome_infant', u'infantstoolcollection', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(110L, u'microbiome_infant', u'infantcircumcision', NOT_REQUIRED, ADDITIONAL),
            EntryTuple(200L, u'microbiome_infant', u'infantdeath', NOT_REQUIRED, ADDITIONAL),
            EntryTuple(240L, u'microbiome_infant', u'infantoffstudy', NOT_REQUIRED, ADDITIONAL))}

    visit_definitions['2090'] = {
        'title': 'Infant 9 Month Visit',
        'time_point': 90,
        'base_interval': 0,
        'base_interval_unit': 'M',
        'window_lower_bound': 0,
        'window_lower_bound_unit': 'D',
        'window_upper_bound': 0,
        'window_upper_bound_unit': 'D',
        'grouping': 'infant',
        'visit_tracking_model': InfantVisit,
        'schedule_group': 'Infant Enrollment',
        'instructions': None,
        'requisitions': (
            RequisitionPanelTuple(300L, u'microbiome_lab', u'infantrequisition',
                                  'DNA PCR', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
            RequisitionPanelTuple(400L, u'microbiome_lab', u'infantrequisition',
                                  'Stool storage', 'STORAGE', 'ST', REQUIRED, NOT_ADDITIONAL),
            RequisitionPanelTuple(500L, u'microbiome_lab', u'infantrequisition',
                                  'Rectal swab (Storage)', 'STORAGE', 'RS', REQUIRED, NOT_ADDITIONAL)),
        'entries': (
            EntryTuple(30L, u'microbiome_infant', u'infantfu', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(40L, u'microbiome_infant', u'infantfuphysical', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(50L, u'microbiome_infant', u'infantfudx', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(80L, u'microbiome_infant', u'infantfunewmed', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(80L, u'microbiome_infant', u'infantfuimmunizations', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(90L, u'microbiome_infant', u'infantarvproph', NOT_REQUIRED, ADDITIONAL),
            EntryTuple(100L, u'microbiome_infant', u'infantfeeding', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(110L, u'microbiome_infant', u'infantstoolcollection', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(110L, u'microbiome_infant', u'infantcircumcision', NOT_REQUIRED, ADDITIONAL),
            EntryTuple(200L, u'microbiome_infant', u'infantdeath', NOT_REQUIRED, ADDITIONAL),
            EntryTuple(240L, u'microbiome_infant', u'infantoffstudy', NOT_REQUIRED, ADDITIONAL))}

    visit_definitions['2120'] = {
        'title': 'Infant 12 Month Visit',
        'time_point': 120,
        'base_interval': 0,
        'base_interval_unit': 'M',
        'window_lower_bound': 0,
        'window_lower_bound_unit': 'D',
        'window_upper_bound': 0,
        'window_upper_bound_unit': 'D',
        'grouping': 'infant',
        'visit_tracking_model': InfantVisit,
        'schedule_group': 'Infant Enrollment',
        'instructions': None,
        'requisitions': (
            RequisitionPanelTuple(300L, u'microbiome_lab', u'infantrequisition',
                                  'DNA PCR', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
            RequisitionPanelTuple(400L, u'microbiome_lab', u'infantrequisition',
                                  'Stool storage', 'STORAGE', 'ST', REQUIRED, NOT_ADDITIONAL),
            RequisitionPanelTuple(500L, u'microbiome_lab', u'infantrequisition',
                                  'Rectal swab (Storage)', 'STORAGE', 'RS', REQUIRED, NOT_ADDITIONAL)),
        'entries': (
            EntryTuple(30L, u'microbiome_infant', u'infantfu', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(40L, u'microbiome_infant', u'infantfuphysical', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(50L, u'microbiome_infant', u'infantfudx', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(80L, u'microbiome_infant', u'infantfunewmed', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(80L, u'microbiome_infant', u'infantfuimmunizations', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(90L, u'microbiome_infant', u'infantarvproph', NOT_REQUIRED, ADDITIONAL),
            EntryTuple(100L, u'microbiome_infant', u'infantfeeding', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(110L, u'microbiome_infant', u'infantstoolcollection', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(110L, u'microbiome_infant', u'infantcircumcision', NOT_REQUIRED, ADDITIONAL),
            EntryTuple(200L, u'microbiome_infant', u'infantdeath', NOT_REQUIRED, ADDITIONAL),
            EntryTuple(240L, u'microbiome_infant', u'infantoffstudy', NOT_REQUIRED, ADDITIONAL))}

site_visit_schedules.register(InfantBirthVisitSchedule)
