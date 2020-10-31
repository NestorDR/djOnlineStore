# Django is a high-level Python Web framework.
# django.contrib: this module has a variety of extra, optional tools that solve common Web-development problems.
from django.contrib import admin

from .models import Service, Category, Post


class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


# Register your models here, to see in Admin Panel of the website
admin.site.register(Service, ServiceAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
