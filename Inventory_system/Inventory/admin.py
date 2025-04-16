from django.contrib import admin
from django.contrib.auth.models import User
from .models import Product,Category,Sales,SalesDetail

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

admin.site.register(Category, CategoryAdmin)

# Register Product model
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category_name', 'created_at', 'updated_at')
    search_fields = ('name',)
    ordering = ('name',)
    def category_name(self, obj):
        return obj.category.name

admin.site.register(Product, ProductAdmin)

# Register Sales model
class SalesAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_amount', 'payment_method', 'sale_date')
    list_filter = ('payment_method', 'sale_date')
    search_fields = ('user__username', 'payment_method')
    ordering = ('sale_date',)

admin.site.register(Sales, SalesAdmin)

# Register SalesDetail model
class SalesDetailAdmin(admin.ModelAdmin):
    list_display = ('sale_id', 'product_name', 'quantity_sold', 'price', 'total_price')
    list_filter = ('sale',)
    search_fields = ('sale__id', 'product__name')
    def product_name(self, obj):
        return obj.product.name
    def sale_id(self, obj):
        return obj.sale.id

admin.site.register(SalesDetail, SalesDetailAdmin)

