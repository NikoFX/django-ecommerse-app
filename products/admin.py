from django.contrib import admin
from .models import Products, Discounts, Popular

# Register your models here.
admin.site.register(Popular)

@admin.register(Products)

class ProductsAdmin(admin.ModelAdmin):

    actions = ['delete_selected', 'status_off', 'status_onn', 'discount1', 'discount2', 'discount3']
    def status_off(self, request, queryset):
        queryset.update(status=0)
    status_off.short_description = "Make hidden"
    def status_onn(self, request, queryset):
        queryset.update(status=1)
    status_onn.short_description = "Make Visible"
    def discount1(self, request, queryset):
        d = Discounts.objects.get(id=0)
        queryset.update(discount_precent=d.precent)
        p = Products.objects.filter(discount_precent__gt=0)
        for i in p:
            price = i.price
            d_p = i.price_discount
            d_s = i.discount_precent
            i.price_discount = price - ((price*d_s) / 100)
            i.save()
    discount1.short_description = 'Discount №1'
    def discount2(self, request, queryset):
        d = Discounts.objects.get(id=1)
        queryset.update(discount_precent=d.precent)
        p = Products.objects.filter(discount_precent__gt=0)
        for i in p:
            price = i.price
            d_p = i.price_discount
            d_s = i.discount_precent
            i.price_discount = price - ((price * d_s) / 100)
            i.save()
    discount2.short_description = 'Discount №2'
    def discount3(self, request, queryset):
        d = Discounts.objects.get(id=2)
        queryset.update(discount_precent=d.precent)
        p = Products.objects.filter(discount_precent__gt=0)
        for i in p:
            price = i.price
            d_p = i.price_discount
            d_s = i.discount_precent
            i.price_discount = price - ((price * d_s) / 100)
            i.save()
    discount3.short_description = 'Discount №3'


    search_fields = ['name']
    list_filter = ['company', 'category', 'discount','status']

    list_display = ['name', 'price', 'price_discount', 'discount_precent', 'discount', 'status']
    list_editable = ['price', 'price_discount', 'status']

    readonly_fields = ['discount']

    class Meta:
        model = Products

@admin.register(Discounts)
class DiscountsAdmin(admin.ModelAdmin):

    list_display = ['name', 'precent', 'end_date']
    fields = ['name', 'precent', 'end_date']
    readonly_fields = ['name']

    admin.site.disable_action('delete_selected')

    class Meta:
        model = Discounts

    def has_delete_permission(self, request, obj=None):
        return False
    def has_add_permission(self, request):
        return False
