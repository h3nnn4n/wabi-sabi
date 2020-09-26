from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from django.utils.html import format_html

from .models import Event, Habit


# Copy paste from https://stackoverflow.com/a/62434674
def linkify(field_name):
    def _linkify(obj):
        content_type = ContentType.objects.get_for_model(obj)
        app_label = content_type.app_label
        linked_obj = getattr(obj, field_name)
        linked_content_type = ContentType.objects.get_for_model(linked_obj)
        model_name = linked_content_type.model
        view_name = f"admin:{app_label}_{model_name}_change"
        link_url = reverse(view_name, args=[linked_obj.pk])
        return format_html('<a href="{}">{}</a>', link_url, linked_obj)

    _linkify.short_description = field_name.replace("_", " ").capitalize()
    return _linkify


class EventInline(admin.TabularInline):
    model = Event
    extra = 0


class HabitAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_filter = ['created_at']
    list_display = ['name', 'created_at']
    inlines = [EventInline]


class EventAdmin(admin.ModelAdmin):
    search_fields = ['notes']
    list_filter = ['created_at']
    list_display = [
        'notes',
        linkify(field_name='habit'),
        'created_at'
    ]


admin.site.register(Habit, HabitAdmin)
admin.site.register(Event, EventAdmin)
