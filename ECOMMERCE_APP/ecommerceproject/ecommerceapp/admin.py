from django.contrib import admin

from ecommerceapp.models import Category, Product

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('cname',)}
admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('pname',)}
admin.site.register(Product,ProductAdmin)