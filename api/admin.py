from django.contrib import admin

from .models import Training, Content, TrainingType


class ContentInline(admin.TabularInline):
    model = Content
    fk_name = "id_training"
    extra = 5


class TrainingAdmin(admin.ModelAdmin):
    fieldsets = [
        ('ABOUT', {'fields': ['evaluation', 'review']}),
        (None, {'fields': ['place', 'created_at']}),
    ]
    inlines = [ContentInline]
    list_display = ('created_at', 'place', 'evaluation', 'review')
    list_filter = ['created_at', 'place']
    search_fields = ['created_at', 'place']


class ContentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['training_type', 'weight', 'id_training']}),
        ('rep number', {'fields': ['set1', 'set2', 'set3']})
    ]
    list_display = ('training_type', 'weight_amounts', 'id_training', 'weight_is_enough')
    list_filter = ['training_type', 'weight', 'id_training']
    search_fields = ['training_type', "id_training"]


class TrainingTypeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['type']}),
    ]
    list_display = ('type',)


class MemoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('ABOUT', {'fields': ['title', 'category', 'created_at']}),
        ('TEXT', {'fields': ['memo']}),
    ]


admin.site.register(Content, ContentAdmin)

admin.site.register(Training, TrainingAdmin)

admin.site.register(TrainingType, TrainingTypeAdmin)

