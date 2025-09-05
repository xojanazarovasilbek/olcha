from django.contrib import admin
from olcha.models import Category, Product, Image
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price")


admin.site.register(Product, ProductAdmin)


admin.site.register(Image)

