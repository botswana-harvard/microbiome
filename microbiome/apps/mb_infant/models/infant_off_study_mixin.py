from edc_offstudy.models.off_study_mixin import OffStudyMixin


class InfantOffStudyMixin(OffStudyMixin):

    OFF_STUDY_MODEL = ('mb_infant
', 'InfantOffStudy')

    class Meta:
        abstract = True