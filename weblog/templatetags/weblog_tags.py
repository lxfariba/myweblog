from django.template.library import Library
import re

__author__ = 'Elfix'

register = Library()


@register.filter("summary", is_safe=True)
def content_summary(content):
    hr_place = content.find("<hr")
    return content[0:hr_place]


@register.filter("removehr", is_safe=True)
def remove_hr(content):
    return re.sub(r'<hr\s*/?>', '<br/>', content)
