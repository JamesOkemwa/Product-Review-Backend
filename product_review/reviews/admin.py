from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Product, Category, Company, ProductSize, ProductSite, Comment

#admin.register() decorator
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'content', )
    list_filter = ('category', )

# Register your models here.
admin.site.register((Category, Company, ProductSize, ProductSite, Comment, ))

admin.site.unregister(Group)

admin.site.site_header = "Product Review Admin"
