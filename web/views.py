from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from models import *

# Create your views here.

def page(request,id=0):
	pages = Page.objects.all()
	try:
		page = Page.objects.get(id=id)
	except:
		page = Page()
		page.name = "404 ERROR"
		page.text = "Not found!"


	return render( request, 'page.html',
		{'pages':pages,'page':page} )

