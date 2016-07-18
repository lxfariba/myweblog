from django.contrib import admin
from .models import Content


class ContentAdmin(admin.ModelAdmin):
    change_form_template = 'weblog/admin/change_form.html'


admin.site.register(Content, ContentAdmin)
