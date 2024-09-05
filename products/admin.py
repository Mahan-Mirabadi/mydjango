from django.contrib import admin
from .models import Product,ProductCategory,ProductInfo

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price' ,'is_active', 'slug', 'ratings' )  # Fields to display
    list_display_links = None
    list_editable = ('description','title', 'price', 'is_active')  # Make description field editable inline
    prepopulated_fields = {'slug': ('title',)}
    list_filter =  ['is_active', 'price']
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(ProductInfo)
