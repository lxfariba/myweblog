__author__ = 'Elfix'
"""
What is a Context Processor in django ?
every time a view wants to load a template it sends a dictionary of values to templates , this dictionary
contains all the require values templates needs to display.
But what if we have some values which we like to show on all pages ?in other words values that are required by
all the templates ? the answer is context processor
read more about context processors :
Django docs : https://docs.djangoproject.com/en/1.9/ref/templates/api/#subclassing-context-requestcontext
More descriptions : http://www.djangobook.com/en/2.0/chapter09.html
"""


def get_post_count(request):
    from weblog.models import Content
    count = Content.objects.count()
    return {
        "global": {
            "contents_count": count
        }
    }
