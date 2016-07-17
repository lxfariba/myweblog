from django.shortcuts import render
from weblog.models import Content
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from weblog.services import convert_month_name_to_date_range


def home(request):
    filters = {}
    if 'month' in request.GET:
        try:
            date_range = convert_month_name_to_date_range(request.GET['month'])
            filters["publish_date__range"] = date_range
        except ValueError:
            # invalid value has been provided for month so ignoring the parameter
            pass
    page = int(request.GET.get('page', '1'))
    content_list = Content.objects.filter(**filters).all().order_by('-id')
    paginator = Paginator(content_list, 5)
    try:
        contents = paginator.page(page)
    except(EmptyPage, InvalidPage):
        contents = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'contents': contents, 'contents_list': content_list})


# def archive(request, arc):
#     arch = Content.objects.get(id=arc)
#     content = Content.objects.all().filter(publish_date__month=date.month)
#     return render(request, 'archive.html', {'content':content, 'arch':arch} )


def post(request, cid):
    content = Content.objects.get(id=cid)
    return render(request, 'post.html', {'content': content})
