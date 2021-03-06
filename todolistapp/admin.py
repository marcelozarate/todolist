# -*- coding: utf-8 *-*
from django.contrib import admin
from todolistapp.models import Task, Category


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class TaskAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}    # Se encarga de rellenar auto
    date_hierarchy = "limit_date"
    fieldsets = (
        (None, {
            'fields': (('title', 'slug'), 'description',
                ('owner', 'category'), ('limit_date')),
        }),
    )
    list_display = ['title', 'creation_date', 'owner']
    list_filter = ['category']
    search_fields = ('title', 'description',)


admin.site.register(Task, TaskAdmin)
admin.site.register(Category, CategoryAdmin)
