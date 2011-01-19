from django.contrib import admin
from blackbook.models import Category, Picture

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}

class PictureAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Picture, PictureAdmin)
