from django.contrib import admin
from django.core.exceptions import PermissionDenied
from .models import (
    Drug,
    Sale,
    Stocked,
    Measurement,
    LockedProduct,
    MarketingItem,
    IssuedItem,
    PickingList,
    Cannister,
    IssuedCannister,
    Client,
)


class DrugAdmin(admin.ModelAdmin):
    list_display = ('name', 'batch_no', 'stock', 'expiry_date')
    search_fields = ('name', 'batch_no')


class SaleAdmin(admin.ModelAdmin):
    list_display = ('drug_sold', 'client', 'batch_no', 'date_sold', 'quantity')
    search_fields = ('drug_sold', 'batch_no', 'client__name')


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email')
    search_fields = ('name', 'phone', 'email')


class MarketingItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'stock')
    search_fields = ('name',)


class IssuedItemAdmin(admin.ModelAdmin):
    list_display = ('item', 'issued_to', 'quantity_issued', 'date_issued', 'issued_by')
    search_fields = ('item', 'issued_to', 'issued_by__username')


class StockedAdmin(admin.ModelAdmin):
    list_display = ('drug_name', 'supplier', 'staff', 'date_added', 'number_added')
    search_fields = ('drug_name__name', 'supplier', 'staff__username')


class PickingListAdmin(admin.ModelAdmin):
    list_display = ('date', 'client', 'product', 'batch_no', 'quantity')
    search_fields = ('product', 'client__name', 'batch_no')


class CannisterAdmin(admin.ModelAdmin):
    list_display = ('name', 'batch_no', 'stock')
    search_fields = ('name', 'batch_no')


class IssuedCannisterAdmin(admin.ModelAdmin):
    list_display = ('name', 'batch_no', 'client', 'date_issued', 'date_returned')
    search_fields = ('name', 'batch_no', 'client__name')


class LockedProductAdmin(admin.ModelAdmin):
    list_display = ('drug', 'locked_by', 'date_locked', 'quantity', 'client')
    search_fields = ('drug__name', 'locked_by__username', 'client__name')

    def save_model(self, request, obj, form, change):
        if change:
            original = LockedProduct.objects.get(pk=obj.pk)
            if original.date_locked and obj.drug != original.drug:
                raise PermissionDenied("Cannot update locked drugs.")
        super().save_model(request, obj, form, change)


admin.site.register(Drug, DrugAdmin)
admin.site.register(Sale, SaleAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(MarketingItem, MarketingItemAdmin)
admin.site.register(IssuedItem, IssuedItemAdmin)
admin.site.register(Stocked, StockedAdmin)
admin.site.register(LockedProduct, LockedProductAdmin)
admin.site.register(PickingList, PickingListAdmin)
admin.site.register(Cannister, CannisterAdmin)
admin.site.register(IssuedCannister, IssuedCannisterAdmin)