from django.contrib import admin
from .models import Title

# Register your models here.


@admin.register(Title)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'priority']
    list_editable = ['title', 'priority']
    search_fields = ['title']
    ordering = ['priority']
