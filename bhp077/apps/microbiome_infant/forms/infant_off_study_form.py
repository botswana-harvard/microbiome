from django import forms
from ..forms import BaseInfantModelForm

from ..models import InfantOffStudy
from bhp077.apps.microbiome_infant.infant_choices import OFF_STUDY_REASON

class InfantOffStudyForm(BaseInfantModelForm):

    reason = forms.ChoiceField(
        label='Please code the primary reason participant taken off-study',
        choices=[choice for choice in OFF_STUDY_REASON],
        help_text="",
        widget=AdminRadioSelect(renderer=AdminRadioFieldRenderer),
    )

    class Meta:
        model = InfantOffStudy
        fields = '__all__'
