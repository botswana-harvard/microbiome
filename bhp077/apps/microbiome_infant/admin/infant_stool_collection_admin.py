from django.contrib import admin

from edc_admin_exclude import AdminExcludeFieldsMixin
from edc_base.modeladmin.admin import BaseModelAdmin

from ..forms import InfantStoolCollectionForm
from ..models import InfantStoolCollection, InfantVisit


class InfantStoolCollectionAdmin(BaseModelAdmin):

    visit_model = InfantVisit
    visit_attr = 'infant_visit'

    fields = ('infant_visit',
              'report_datetime',
              'sample_obtained',
              'nappy_type',
              'other_nappy',
              'stool_collection',
              'stool_collection_time',
              'stool_stored',
              'past_diarrhea',
              'diarrhea_past_24hrs',
              'antibiotics_7days',
              'antibiotic_dose_24hrs',)

    form = InfantStoolCollectionForm
    radio_fields = {
        "sample_obtained": admin.VERTICAL,
        "nappy_type": admin.VERTICAL,
        "stool_collection": admin.VERTICAL,
        "stool_stored": admin.VERTICAL,
        "past_diarrhea": admin.VERTICAL,
        "diarrhea_past_24hrs": admin.VERTICAL,
        "antibiotics_7days": admin.VERTICAL,
        "antibiotic_dose_24hrs": admin.VERTICAL}

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "infant_visit":
                kwargs["queryset"] = InfantVisit.objects.filter(id=request.GET.get('infant_visit'))
        return super(InfantStoolCollectionAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(InfantStoolCollection, InfantStoolCollectionAdmin)
