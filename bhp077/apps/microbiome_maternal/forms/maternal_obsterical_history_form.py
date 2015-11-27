from django import forms
from base_maternal_model_form import BaseMaternalModelForm

from ..models import MaternalObstericalHistory


class MaternalObstericalHistoryForm(BaseMaternalModelForm):

    def clean(self):
        cleaned_data = super(MaternalObstericalHistoryForm, self).clean()

        if cleaned_data.get('pregs_24wks_or_more') > 0:
            if (
                cleaned_data.get('lost_after_24wks') == 0 and
                cleaned_data.get('live_children') == 0 and
                cleaned_data.get('children_died_b4_5yrs') == 0
            ):
                raise forms.ValidationError('You indicated previous at least 24 weeks were {}. '
                                            'Number of pregnancies least 24 weeks,'
                                            'number of pregnancies lost before 24 weeks,'
                                            'number of pregnancies lost at or after 24 weeks.'
                                            .format(cleaned_data.get('pregs_24wks_or_more')))
        if cleaned_data.get('prev_pregnancies') > 0:
            if (
                cleaned_data.get('pregs_24wks_or_more') == 0 and
                cleaned_data.get('lost_before_24wks') == 0 and
                cleaned_data.get('lost_after_24wks') == 0
            ):
                raise forms.ValidationError('You indicated previous pregancies were {}. '
                                            'Number of pregnancies at or after 24 weeks,'
                                            'number of living children,'
                                            'number of children died after 5 year CANNOT all be zero.'
                                            .format(cleaned_data.get('prev_pregnancies')))
        return cleaned_data

    class Meta:
        model = MaternalObstericalHistory
        fields = '__all__'
