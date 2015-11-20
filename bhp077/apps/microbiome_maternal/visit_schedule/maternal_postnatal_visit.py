from collections import OrderedDict

from edc.subject.visit_schedule.classes import (VisitScheduleConfiguration, site_visit_schedules,
                                                EntryTuple, MembershipFormTuple,
                                                ScheduleGroupTuple, RequisitionPanelTuple)
from edc_constants.constants import REQUIRED, NOT_REQUIRED, ADDITIONAL, NOT_ADDITIONAL

from ..models import MaternalVisit, PostnatalEnrollment


class PostnatalEnrollmentVisitSchedule(VisitScheduleConfiguration):

    name = 'postnatal visit schedule'
    app_label = 'microbiome_maternal'

    membership_forms = OrderedDict({'postnatal': MembershipFormTuple(
        'postnatal', PostnatalEnrollment, True), })

    schedule_groups = OrderedDict({
        'Postnatal Enrollment': ScheduleGroupTuple('Postnatal Enrollment',
                                                   'postnatal', None, None), })

    visit_definitions = OrderedDict()

    visit_definitions['1000M'] = {
        'title': 'Maternal Postnatal Enrollment',
        'time_point': 0,
        'base_interval': 0,
        'base_interval_unit': 'D',
        'window_lower_bound': 0,
        'window_lower_bound_unit': 'D',
        'window_upper_bound': 0,
        'window_upper_bound_unit': 'D',
        'grouping': '',
        'visit_tracking_model': MaternalVisit,
        'schedule_group': 'Postnatal Enrollment',
        'instructions': '',
        'requisitions': (),
        'entries': (
            EntryTuple(10L, u'microbiome_maternal', u'maternallocator', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(20L, u'microbiome_maternal', u'maternaldemographics', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(30L, u'microbiome_maternal', u'maternalmedicalhistory', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(40L, u'microbiome_maternal', u'maternalobstericalhistory', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(50L, u'microbiome_maternal', u'maternalclinicalhistory', NOT_REQUIRED, NOT_ADDITIONAL),
            EntryTuple(60L, u'microbiome_maternal', u'maternalarvhistory', NOT_REQUIRED, ADDITIONAL),
            EntryTuple(70L, u'microbiome_maternal', u'maternalarvpreg', NOT_REQUIRED, ADDITIONAL),
            EntryTuple(80L, u'microbiome_maternal', u'maternalinfected', NOT_REQUIRED, ADDITIONAL),
            EntryTuple(90L, u'microbiome_maternal', u'maternaluninfected', NOT_REQUIRED, ADDITIONAL),
            EntryTuple(100L, u'microbiome_maternal', u'maternalbreasthealth', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(200L, u'microbiome_maternal', u'maternaldeath', NOT_REQUIRED, ADDITIONAL),
            EntryTuple(210L, u'microbiome_maternal', u'maternaloffstudy', NOT_REQUIRED, ADDITIONAL), )}

    visit_definitions['2000M'] = {
        'title': 'Maternal Delivery',
        'time_point': 0,
        'base_interval': 0,
        'base_interval_unit': 'D',
        'window_lower_bound': 0,
        'window_lower_bound_unit': 'D',
        'window_upper_bound': 0,
        'window_upper_bound_unit': 'D',
        'grouping': '',
        'visit_tracking_model': MaternalVisit,
        'schedule_group': 'Postnatal Enrollment',
        'instructions': '',
        'requisitions': (
            RequisitionPanelTuple(10L, u'microbiome_lab', u'maternalrequisition',
                                  'Viral Load', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
            RequisitionPanelTuple(20L, u'microbiome_lab', u'maternalrequisition',
                                  'Breast Milk (Storage)', 'STORAGE', 'BM', REQUIRED, NOT_ADDITIONAL),
            RequisitionPanelTuple(30L, u'microbiome_lab', u'maternalrequisition',
                                  'Vaginal swab (Storage)', 'STORAGE', 'VS', REQUIRED, NOT_ADDITIONAL),
            RequisitionPanelTuple(40L, u'microbiome_lab', u'maternalrequisition',
                                  'Rectal swab (Storage)', 'STORAGE', 'RS', REQUIRED, NOT_ADDITIONAL),
            RequisitionPanelTuple(50L, u'microbiome_lab', u'maternalrequisition',
                                  'Skin Flora (Storage)', 'STORAGE', 'SF', REQUIRED, NOT_ADDITIONAL),
            RequisitionPanelTuple(60L, u'microbiome_lab', u'maternalrequisition',
                                  'Vaginal Swab (multiplex PCR)', 'TEST', 'VM', REQUIRED, NOT_ADDITIONAL)),
        'entries': (
            EntryTuple(10L, u'microbiome_maternal', u'maternallabourdel', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(20L, u'microbiome_maternal', u'maternallabdelmed', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(30L, u'microbiome_maternal', u'maternallabdelclinic', NOT_REQUIRED, ADDITIONAL),
            EntryTuple(40L, u'microbiome_maternal', u'maternallabdeldx', NOT_REQUIRED, ADDITIONAL),
            EntryTuple(50L, u'microbiome_maternal', u'maternalarvpreg', NOT_REQUIRED, ADDITIONAL),
            EntryTuple(60L, u'microbiome_maternal', u'maternalarv', NOT_REQUIRED, ADDITIONAL),
            EntryTuple(100L, u'microbiome_maternal', u'maternalbreasthealth', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(200L, u'microbiome_maternal', u'maternaldeath', NOT_REQUIRED, ADDITIONAL),
            EntryTuple(210L, u'microbiome_maternal', u'maternaloffstudy', NOT_REQUIRED, ADDITIONAL), )}

    visit_definitions['2010M'] = {
        'title': '1 Month Visit',
        'time_point': 10,
        'base_interval': 1,
        'base_interval_unit': 'M',
        'window_lower_bound': 15,
        'window_lower_bound_unit': 'D',
        'window_upper_bound': 60,
        'window_upper_bound_unit': 'D',
        'grouping': '',
        'visit_tracking_model': MaternalVisit,
        'schedule_group': 'Postnatal Enrollment',
        'instructions': None,
        'requisitions': (
            RequisitionPanelTuple(10L, u'microbiome_lab', u'maternalrequisition',
                                  'Viral Load', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
            RequisitionPanelTuple(20L, u'microbiome_lab', u'maternalrequisition',
                                  'Breast Milk (Storage)', 'STORAGE', 'BM', REQUIRED, NOT_ADDITIONAL)),
        'entries': (
            EntryTuple(10L, u'microbiome_maternal', u'maternalpostfu', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(20L, u'microbiome_maternal', u'maternalpostfudx', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(25L, u'microbiome_maternal', u'maternalpostfumed', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(30L, u'microbiome_maternal', u'sexualreproductivehealth', NOT_REQUIRED, ADDITIONAL),
            EntryTuple(40L, u'microbiome_maternal', u'srhservicesutilization', NOT_REQUIRED, ADDITIONAL),
            EntryTuple(50L, u'microbiome_maternal', u'maternalarvpost', NOT_REQUIRED, ADDITIONAL),
            EntryTuple(60L, u'microbiome_maternal', u'maternalarvpostadh', NOT_REQUIRED, ADDITIONAL),
            EntryTuple(65L, u'microbiome_maternal', u'maternalbreasthealth', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(70L, u'microbiome_maternal', u'rapidtestresult', NOT_REQUIRED, ADDITIONAL),
            EntryTuple(200L, u'microbiome_maternal', u'maternaldeath', NOT_REQUIRED, ADDITIONAL),
            EntryTuple(210L, u'microbiome_maternal', u'maternaloffstudy', NOT_REQUIRED, ADDITIONAL), )}

    visit_definitions['2030M'] = {
        'title': '3 Months Visit',
        'time_point': 30,
        'base_interval': 3,
        'base_interval_unit': 'M',
        'window_lower_bound': 29,
        'window_lower_bound_unit': 'D',
        'window_upper_bound': 45,
        'window_upper_bound_unit': 'D',
        'grouping': '',
        'visit_tracking_model': MaternalVisit,
        'schedule_group': 'Postnatal Enrollment',
        'instructions': None,
        'requisitions': (
            RequisitionPanelTuple(10L, u'microbiome_lab', u'maternalrequisition',
                                  'Viral Load', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
            RequisitionPanelTuple(20L, u'microbiome_lab', u'maternalrequisition',
                                  'Breast Milk (Storage)', 'STORAGE', 'BM', NOT_REQUIRED, ADDITIONAL)),
        'entries': (
            EntryTuple(10L, u'microbiome_maternal', u'maternalpostfu', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(20L, u'microbiome_maternal', u'maternalpostfudx', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(25L, u'microbiome_maternal', u'maternalpostfumed', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(30L, u'microbiome_maternal', u'sexualreproductivehealth', NOT_REQUIRED, ADDITIONAL),
            EntryTuple(40L, u'microbiome_maternal', u'srhservicesutilization', NOT_REQUIRED, ADDITIONAL),
            EntryTuple(50L, u'microbiome_maternal', u'maternalarvpost', NOT_REQUIRED, ADDITIONAL),
            EntryTuple(60L, u'microbiome_maternal', u'maternalarvpostadh', NOT_REQUIRED, ADDITIONAL),
            EntryTuple(65L, u'microbiome_maternal', u'maternalbreasthealth', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(70L, u'microbiome_maternal', u'rapidtestresult', NOT_REQUIRED, ADDITIONAL),
            EntryTuple(200L, u'microbiome_maternal', u'maternaldeath', NOT_REQUIRED, ADDITIONAL),
            EntryTuple(210L, u'microbiome_maternal', u'maternaloffstudy', NOT_REQUIRED, ADDITIONAL), )}

    visit_definitions['2060M'] = {
        'title': '6 Months Visit',
        'time_point': 60,
        'base_interval': 6,
        'base_interval_unit': 'M',
        'window_lower_bound': 44,
        'window_lower_bound_unit': 'D',
        'window_upper_bound': 45,
        'window_upper_bound_unit': 'D',
        'grouping': '',
        'visit_tracking_model': MaternalVisit,
        'schedule_group': 'Postnatal Enrollment',
        'instructions': None,
        'requisitions': (
            RequisitionPanelTuple(10L, u'microbiome_lab', u'maternalrequisition',
                                  'Viral Load', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
            RequisitionPanelTuple(20L, u'microbiome_lab', u'maternalrequisition',
                                  'Breast Milk (Storage)', 'STORAGE', 'BM', NOT_REQUIRED, ADDITIONAL)),
        'entries': (
            EntryTuple(10L, u'microbiome_maternal', u'maternalpostfu', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(20L, u'microbiome_maternal', u'maternalpostfudx', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(25L, u'microbiome_maternal', u'maternalpostfumed', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(30L, u'microbiome_maternal', u'sexualreproductivehealth', NOT_REQUIRED, ADDITIONAL),
            EntryTuple(40L, u'microbiome_maternal', u'srhservicesutilization', NOT_REQUIRED, ADDITIONAL),
            EntryTuple(50L, u'microbiome_maternal', u'maternalarvpost', NOT_REQUIRED, ADDITIONAL),
            EntryTuple(60L, u'microbiome_maternal', u'maternalarvpostadh', NOT_REQUIRED, ADDITIONAL),
            EntryTuple(65L, u'microbiome_maternal', u'maternalbreasthealth', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(70L, u'microbiome_maternal', u'rapidtestresult', NOT_REQUIRED, ADDITIONAL),
            EntryTuple(200L, u'microbiome_maternal', u'maternaldeath', NOT_REQUIRED, ADDITIONAL),
            EntryTuple(210L, u'microbiome_maternal', u'maternaloffstudy', NOT_REQUIRED, ADDITIONAL), )}

    visit_definitions['2090M'] = {
        'title': '9 Months Visit',
        'time_point': 90,
        'base_interval': 9,
        'base_interval_unit': 'M',
        'window_lower_bound': 44,
        'window_lower_bound_unit': 'D',
        'window_upper_bound': 45,
        'window_upper_bound_unit': 'D',
        'grouping': '',
        'visit_tracking_model': MaternalVisit,
        'schedule_group': 'Postnatal Enrollment',
        'instructions': None,
        'requisitions': (
            RequisitionPanelTuple(10L, u'microbiome_lab', u'maternalrequisition',
                                  'Viral Load', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
            RequisitionPanelTuple(20L, u'microbiome_lab', u'maternalrequisition',
                                  'Breast Milk (Storage)', 'STORAGE', 'BM', NOT_REQUIRED, ADDITIONAL)),
        'entries': (
            EntryTuple(10L, u'microbiome_maternal', u'maternalpostfu', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(20L, u'microbiome_maternal', u'maternalpostfudx', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(25L, u'microbiome_maternal', u'maternalpostfumed', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(30L, u'microbiome_maternal', u'sexualreproductivehealth', NOT_REQUIRED, ADDITIONAL),
            EntryTuple(40L, u'microbiome_maternal', u'srhservicesutilization', NOT_REQUIRED, ADDITIONAL),
            EntryTuple(50L, u'microbiome_maternal', u'maternalarvpost', NOT_REQUIRED, ADDITIONAL),
            EntryTuple(60L, u'microbiome_maternal', u'maternalarvpostadh', NOT_REQUIRED, ADDITIONAL),
            EntryTuple(65L, u'microbiome_maternal', u'maternalbreasthealth', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(70L, u'microbiome_maternal', u'rapidtestresult', NOT_REQUIRED, ADDITIONAL),
            EntryTuple(200L, u'microbiome_maternal', u'maternaldeath', NOT_REQUIRED, ADDITIONAL),
            EntryTuple(210L, u'microbiome_maternal', u'maternaloffstudy', NOT_REQUIRED, ADDITIONAL), )}

    visit_definitions['2120M'] = {
        'title': '12 Months Visit',
        'time_point': 120,
        'base_interval': 12,
        'base_interval_unit': 'M',
        'window_lower_bound': 44,
        'window_lower_bound_unit': 'D',
        'window_upper_bound': 45,
        'window_upper_bound_unit': 'D',
        'grouping': '',
        'visit_tracking_model': MaternalVisit,
        'schedule_group': 'Postnatal Enrollment',
        'instructions': None,
        'requisitions': (
            RequisitionPanelTuple(10L, u'microbiome_lab', u'maternalrequisition',
                                  'Viral Load', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
            RequisitionPanelTuple(20L, u'microbiome_lab', u'maternalrequisition',
                                  'Breast Milk (Storage)', 'STORAGE', 'BM', NOT_REQUIRED, ADDITIONAL)),
        'entries': (
            EntryTuple(10L, u'microbiome_maternal', u'maternalpostfu', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(20L, u'microbiome_maternal', u'maternalpostfudx', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(25L, u'microbiome_maternal', u'maternalpostfumed', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(30L, u'microbiome_maternal', u'sexualreproductivehealth', NOT_REQUIRED, ADDITIONAL),
            EntryTuple(40L, u'microbiome_maternal', u'srhservicesutilization', NOT_REQUIRED, ADDITIONAL),
            EntryTuple(50L, u'microbiome_maternal', u'maternalarvpost', NOT_REQUIRED, ADDITIONAL),
            EntryTuple(60L, u'microbiome_maternal', u'maternalarvpostadh', NOT_REQUIRED, ADDITIONAL),
            EntryTuple(65L, u'microbiome_maternal', u'maternalbreasthealth', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(70L, u'microbiome_maternal', u'rapidtestresult', NOT_REQUIRED, ADDITIONAL),
            EntryTuple(200L, u'microbiome_maternal', u'maternaldeath', NOT_REQUIRED, ADDITIONAL),
            EntryTuple(210L, u'microbiome_maternal', u'maternaloffstudy', NOT_REQUIRED, ADDITIONAL), )}
site_visit_schedules.register(PostnatalEnrollmentVisitSchedule)
