from django.shortcuts import render
from weblog.models import Content
from django.core.paginator import Paginator

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
		
	return render(request,'index.html',{'contents':contents})
