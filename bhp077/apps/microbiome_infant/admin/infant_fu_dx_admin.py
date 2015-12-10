from collections import OrderedDict

from django.contrib import admin

from edc.base.modeladmin.admin import BaseTabularInline
from edc.export.actions import export_as_csv_action

from ..models import InfantFuDx, InfantVisit, InfantFuDxItems
from ..forms import InfantFuDxItemsForm

from .base_infant_scheduled_modeladmin import BaseInfantScheduleModelAdmin


class InfantFuDxItemsInline(BaseTabularInline):

    model = InfantFuDxItems
    form = InfantFuDxItemsForm
    extra = 0


class InfantFuDxAdmin(BaseInfantScheduleModelAdmin):

    inlines = [InfantFuDxItemsInline, ]

    actions = [
        export_as_csv_action(
            description="CSV Export of Infant Followup Diagnosis",
            fields=[],
            delimiter=',',
            exclude=['created', 'modified', 'user_created', 'user_modified', 'revision', 'id', 'hostname_created',
                     'hostname_modified'],
            extra_fields=OrderedDict(
                {'subject_identifier': 'infant_visit__appointment__registered_subject__subject_identifier',
                 'gender': 'infant_visit__appointment__registered_subject__gender',
                 'dob': 'infant_visit__appointment__registered_subject__dob',
                 }),
        )]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "infant_visit":
                kwargs["queryset"] = InfantVisit.objects.filter(id=request.GET.get('infant_visit'))
        return super(InfantFuDxAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(InfantFuDx, InfantFuDxAdmin)
