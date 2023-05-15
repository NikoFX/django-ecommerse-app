from django.contrib import admin
from .models import Orders
from .models import Coupons
from .models import Min_order


# Register your models here.
@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'address', 'created_date', 'status')

    fields = ('name', 'phone', 'address', 'product', 'created_date', 'status')
    readonly_fields = ('name', 'phone', 'address', 'product', 'created_date')

    class Meta:
        model = Orders


@admin.register(Coupons)
class CouponsAdmin(admin.ModelAdmin):
    list_display = ('coupon_code', 'discount', 'including')

    fields = ('coupon_code', 'discount', 'including')

    class Meta:
        model = Coupons

@admin.register(Min_order)
class Min_orderAdmin(admin.ModelAdmin):

    list_display = ('name', 'delivery_price', 'price')
    fields = ('delivery_price', 'price')

    def has_delete_permission(self, request, obj=None):
        return False
    def has_add_permission(self, request):
        return False

    class Meta:
        model = Min_order




