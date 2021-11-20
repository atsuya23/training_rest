from django.contrib import admin

from .models import Memo


class MemoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('ABOUT', {'fields': ['title', 'category', 'created_at']}),
        ('TEXT', {'fields': ['memo']}),
    ]


admin.site.register(Memo, MemoAdmin)
