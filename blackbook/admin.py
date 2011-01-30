from django.contrib import admin
from blackbook.models import Category, Photo

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}

class PhotoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Photo, PhotoAdmin)
