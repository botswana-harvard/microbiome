from django import forms

from edc_constants.constants import YES

from base_maternal_model_form import BaseMaternalModelForm

from ..models import (MaternalLabourDel, MaternalLabDelMed,
                      MaternalLabDelClinic, MaternalLabDelDx,
                      MaternalLabDelDxT)


class MaternalLabourDelForm(BaseMaternalModelForm):

    def clean(self):
        cleaned_data = self.cleaned_data
        if cleaned_data.get('live_infants_to_register') > 1:
            raise forms.ValidationError("For this study we can only register ONE infant")
        # Validate that number of live_infants_to_register cannot be 0 or less
        if cleaned_data.get('live_infants_to_register') <= 0:
            raise forms.ValidationError('Number of live infants to register may not be less than or equal to 0!.')
        if cleaned_data.get('delivery_datetime') > cleaned_data.get('report_datetime'):
                raise forms.ValidationError('Maternal Labour Delivery date cannot be greater than report date. '
                                            'Please correct.')
        return super(MaternalLabourDelForm, self).clean()

    class Meta:
        model = MaternalLabourDel
        fields = '__all__'


class MaternalLabDelMedForm(BaseMaternalModelForm):

    def clean(self):
        cleaned_data = super(MaternalLabDelMedForm, self).clean()
        if 'health_cond' in cleaned_data.keys():
            self.validate_m2m(
                label='health condition',
                leading=cleaned_data.get('has_health_cond'),
                m2m=cleaned_data.get('health_cond'),
                other=cleaned_data.get('health_cond_other'))
        if 'ob_comp' in cleaned_data.keys():
            self.validate_m2m(
                label='obstetric complication',
                leading=cleaned_data.get('has_ob_comp'),
                m2m=cleaned_data.get('ob_comp'),
                other=cleaned_data.get('ob_comp_other'))
        if 'suppliments' in cleaned_data.keys():
            self.validate_m2m(
                label='pregnancy suppliment',
                leading=cleaned_data.get('took_suppliments'),
                m2m=cleaned_data.get('suppliments'))
        return cleaned_data

    class Meta:
        model = MaternalLabDelMed
        fields = '__all__'


class MaternalLabDelClinicForm(BaseMaternalModelForm):

    def clean(self):
        cleaned_data = super(MaternalLabDelClinicForm, self).clean()
        # If CD4 performed, date and result should be supplied
        if cleaned_data.get('has_cd4') == YES:
            if not cleaned_data.get('cd4_date'):
                raise forms.ValidationError('You indicated that a CD4 count was performed. Please provide the date.')
            if not cleaned_data.get('cd4_result'):
                raise forms.ValidationError('You indicated that a CD4 count was performed. Please provide the result.')
        else:
            # If cd4 was not performed no date nor result should be provided
            if cleaned_data.get('cd4_date'):
                raise forms.ValidationError('You indicated that a CD4 count was NOT performed, yet provided a date '
                                            'CD4 was performed. Please correct.')
            if cleaned_data.get('cd4_result'):
                raise forms.ValidationError('You indicated that a CD4 count was NOT performed, yet provided a CD4 '
                                            'result. Please correct.')
        # If VL performed, date and result should be supplied
        if cleaned_data.get('has_vl') == YES:
            if not cleaned_data.get('vl_date'):
                raise forms.ValidationError('You indicated that a VL count was performed. Please provide the date.')
            if not cleaned_data.get('vl_result'):
                raise forms.ValidationError('You indicated that a VL count was performed. Please provide the result.')
        else:
            # If VL was not performed, no VL date nor result should be supplied
            if cleaned_data.get('vl_date'):
                raise forms.ValidationError('You indicated that a VL count was NOT performed, yet provided a date VL '
                                            'was performed. Please correct.')
            if cleaned_data.get('vl_result'):
                raise forms.ValidationError('You indicated that a VL count was NOT performed, yet provided a VL result'
                                            ' Please correct.')
        return cleaned_data

    class Meta:
        model = MaternalLabDelClinic
        fields = '__all__'


class MaternalLabDelDxForm(BaseMaternalModelForm):

    class Meta:
        model = MaternalLabDelDx
        fields = '__all__'


class MaternalLabDelDxTForm(BaseMaternalModelForm):

    class Meta:
        model = MaternalLabDelDxT
        fields = '__all__'
