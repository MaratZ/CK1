from django.contrib import admin
from .models import Supplier, Contact, Product

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'country', 'city', 'street', 'house_number')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date')

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'contact', 'debt', 'supplier_link', 'created_at')
    list_filter = ('contact__city', 'level')
    actions = ['clear_debt']

    def supplier_link(self, obj):
        if obj.supplier:
            return f'<a href="/admin/network/supplier/{obj.supplier.id}/">{obj.supplier.name}</a>'
        return "-"
    supplier_link.allow_tags = True
    supplier_link.short_description = "Supplier"

    def clear_debt(self, request, queryset):
        queryset.update(debt=0)
    clear_debt.short_description = "Clear debt for selected suppliers"