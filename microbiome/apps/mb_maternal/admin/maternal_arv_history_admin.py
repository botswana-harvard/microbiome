from django.contrib import admin

from ..forms import MaternalArvHistoryForm
from ..models import MaternalArvHistory

from .base_maternal_model_admin import BaseMaternalModelAdmin


class MaternalArvHistoryAdmin(BaseMaternalModelAdmin):
    form = MaternalArvHistoryForm

    list_display = ('maternal_visit', 'haart_start_date', 'preg_on_haart')

    list_filter = ('preg_on_haart', )

    radio_fields = {
        'preg_on_haart': admin.VERTICAL,
        'prior_preg': admin.VERTICAL,
        'is_date_estimated': admin.VERTICAL}

    filter_horizontal = ('prior_arv', )

admin.site.register(MaternalArvHistory, MaternalArvHistoryAdmin)
