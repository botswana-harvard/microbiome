from django.contrib import admin

from edc_base.modeladmin.admin import BaseModelAdmin
from ..forms import MaternalInfectedForm
from ..models import MaternalInfected


class MaternalInfectedAdmin(BaseModelAdmin):

    form = MaternalInfectedForm
    fields = ('prev_pregnancies',
              'prior_health_haart',
              'prev_pregnancy_arv',
              'know_hiv_status',
              'weight',
              'height',
              'systolic_bp',
              'diastolic_bp')
    list_display = ('prev_pregnancies',
                    'prior_health_haart',
                    'prev_pregnancy_arv')
    list_filter = ('prev_pregnancies',
                   'prior_health_haart',
                   'prev_pregnancy_arv')
    radio_fields = {'prior_health_haart': admin.VERTICAL,
                    'prev_pregnancy_arv': admin.VERTICAL,
                    'know_hiv_status': admin.VERTICAL}
admin.site.register(MaternalInfected, MaternalInfectedAdmin)
