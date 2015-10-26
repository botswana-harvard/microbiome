from django import forms

from edc_constants.constants import NO, YES
from base_maternal_model_form import BaseMaternalModelForm
from ..models import MaternalArvPost, MaternalArvPostMod, MaternalArvPostAdh


class MaternalArvPostForm(BaseMaternalModelForm):

    def clean(self):
        cleaned_data = self.cleaned_data
        # if mother is not supposed to be on ARVS,then the MaternalArvPostAdh is not required
        if cleaned_data.get('haart_last_visit') == NO or cleaned_data.get('arv_status') == 'never started':
            if MaternalArvPostAdh.objects.filter(maternal_visit=cleaned_data.get('maternal_visit')):
                raise forms.ValidationError("ARV history exists. You wrote mother did NOT receive ARVs "
                                            "in this pregnancy. Please correct '%s' first." % MaternalArvPostAdh._meta.verbose_name)

        if cleaned_data.get('haart_last_visit') == NO and cleaned_data.get('haart_reason') != 'N/A':
            raise forms.ValidationError('You indicated that participant was not on HAART.'
                                        ' You CANNOT provide a reason. Please correct.')
        if cleaned_data.get('haart_last_visit') == YES and cleaned_data.get('haart_reason') == 'N/A':
            raise forms.ValidationError("You indicated that participant was on HAART. Reason CANNOT be 'Not Applicable'. Please correct.")

        return super(MaternalArvPostForm, self).clean()

    class Meta:
        model = MaternalArvPost
        fields = '__all__'


class MaternalArvPostModForm(BaseMaternalModelForm):

    def clean(self):
        cleaned_data = self.cleaned_data

        if cleaned_data.get('maternal_arv_post').arv_status == 'N/A' or cleaned_data.get('maternal_arv_post').arv_status == 'no_mod':
            if cleaned_data.get('arv_code'):
                raise forms.ValidationError("You cannot indicate arv modifaction as you indicated {} above.".format(cleaned_data.get('maternal_arv_post').arv_status))
        return super(MaternalArvPostModForm, self).clean()

    class Meta:
        model = MaternalArvPostMod
        fields = '__all__'


class MaternalArvPostAdhForm(BaseMaternalModelForm):

    def clean(self):
        cleaned_data = self.cleaned_data
        if not cleaned_data.get('maternal_visit'):
            raise forms.ValidationError('This field is required. Please fill it in')
        return super(MaternalArvPostAdhForm, self).clean()

    class Meta:
        model = MaternalArvPostAdh
        fields = '__all__'
