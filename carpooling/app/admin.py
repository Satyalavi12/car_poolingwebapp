from django.contrib import admin
from app.models import Userdetails,URL,Trip

admin.site.register(Userdetails)
admin.site.register(URL)
admin.site.register(Trip)

# admin.py
from django.contrib import admin
from django.utils.html import format_html
from .models import MyModel

class MyModelAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-height: 200px; max-width: 200px;" />'.format(obj.image.url))

    image_tag.short_description = 'Image Preview'

    readonly_fields = ('image_tag',)

admin.site.register(MyModel, MyModelAdmin)

