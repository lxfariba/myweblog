from django.shortcuts import render
from weblog.models import Content

def home(request):
	contents = Content.objects.all()
	return render(request,'index.html',{'contents':contents})
