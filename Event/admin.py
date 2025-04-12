from django.contrib.admin import ModelAdmin, TabularInline, register
from django.db.models import JSONField

from Language.widgets.myTranslation_json_widget import MyTranslationWidget
from Event.models import Event, EventType, EventAlbum
from .forms import EventTypeAdminForm

# Register your models here.


class EventAlbumInline(TabularInline):
    model = EventAlbum
    extra = 1


@register(EventType)
class EventTypeAdmin(ModelAdmin):
    form = EventTypeAdminForm
    formfield_overrides = {
        JSONField: {
            "widget": MyTranslationWidget,
        },
    }


@register(Event)
class EventAdmin(ModelAdmin):
    model = Event
    extra = 1
    inlines = [
        EventAlbumInline,
    ]
