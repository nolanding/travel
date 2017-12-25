from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
	return HttpResponse("A hello u know me")

def aindex(request):
	context = {
		"title":"hello im deeksha"
	}
	return render(request,'index.html',context)
	#return HttpResponse("B hello u know me")

def single(request):
	return render(request,'single.html')
def cindex(request):
	return HttpResponse("D hello u know me")
