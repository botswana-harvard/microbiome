from django.contrib import admin

from edc.base.modeladmin.admin import BaseModelAdmin
from edc.base.modeladmin.admin import BaseTabularInline

from bhp077.apps.microbiome_infant.forms import InfantFuNewMedItemsForm, InfantFuNewMedForm
from bhp077.apps.microbiome_infant.models import InfantFuNewMedItems

from ..models import InfantFuNewMed, InfantVisit


class InfantFuNewMedItemsInline(BaseTabularInline):

    model = InfantFuNewMedItems
    form = InfantFuNewMedItemsForm
    extra = 0


class InfantFuNewMedAdmin(BaseModelAdmin):

    radio_fields = {'new_medications': admin.VERTICAL, }
    inlines = [InfantFuNewMedItemsInline, ]
    form = InfantFuNewMedForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "infant_visit":
                kwargs["queryset"] = InfantVisit.objects.filter(id=request.GET.get('infant_visit'))
        return super(InfantFuNewMedAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(InfantFuNewMed, InfantFuNewMedAdmin)
