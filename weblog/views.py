from django.shortcuts import render
from weblog.models import Content
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from datetime import date
from django.db.models import Q


def home(request):
    content_list = Content.objects.all().order_by('-id')
    paginator = Paginator(content_list, 5)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        contents = paginator.page(page)
    except(EmptyPage, InvalidPage):
        contents = paginator.page(paginator.num_pages)

    contents_list = Content.objects.filter(publish_date__range=['2016-07-01','2016-08-01'])

    return render(request, 'index.html', {'contents':contents,'contents_list':contents_list})


# def archive(request, arc):
#     arch = Content.objects.get(id=arc)
#     content = Content.objects.all().filter(publish_date__month=date.month)
#     return render(request, 'archive.html', {'content':content, 'arch':arch} )


def post(request,cid):
    content = Content.objects.get(id=cid)
    return render(request, 'post.html', {'content':content})
