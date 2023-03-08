from django.contrib import admin
from . import models


#Lists projects for admin
@admin.register(models.Project)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'slug', 'creator', 'riskiness')
    prepopulated_fields = {
        'slug': ('title', ),
    }
