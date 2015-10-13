from datetime import datetime

from django.db import models
from django.core.urlresolvers import reverse

from edc_base.model.models import BaseUuidModel
from edc_base.audit_trail import AuditTrail

from .managers import OrderManager


class Order(BaseUuidModel):

    order_datetime = models.DateTimeField(default=datetime.today())

    objects = OrderManager()

    history = AuditTrail()

    def natural_key(self):
        return (self.order_datetime, )

    def items(self):
        change_list_url = reverse("admin:{}_{}_changelist".format(self._meta.app_label, 'orderitem'))
        return '<a href="{change_list_url}?q={pk}">{count} items</a>'.format(
            change_list_url=change_list_url, pk=self.id, count=self.order_items.count())
    items.allow_tags = True

    @property
    def order_items(self):
        OrderItem = models.get_model('lab', 'orderitem')
        return OrderItem.objects.filter(order__pk=self.pk)

    class Meta:
        app_label = 'lab'