from edc.subject.lab_tracker.classes import site_lab_tracker
from edc.subject.lab_tracker.classes import HivLabTracker

from .models import RapidTestResult


class MaternalHivLabTracker(HivLabTracker):
    subject_type = 'maternal'
    trackers = [(RapidTestResult, 'result', 'result_date', )]

site_lab_tracker.register(MaternalHivLabTracker)