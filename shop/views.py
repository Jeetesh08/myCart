from django.shortcuts import render
from django.http import  HttpResponse


# Create your views here.
def index(request):
    return render(request,'shop/index.html')
def about(request):
    return HttpResponse("AboutUs")

def contact(request):
    return HttpResponse("ContactUs")

def tracker(request):
    return HttpResponse("TrackingStatus")

def search(request):
    return HttpResponse("search")

def productview(request):
    return HttpResponse("ProductStatus")

def checkout(request):
    return HttpResponse("checkout")

def index(request):
    objects = Product.objects.all()
    context = {
            'objects' : objects
            }
    return render(request,'shop/index.html',context)

