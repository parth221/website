from django.shortcuts import render
from .models import Product
# Create your views here.
def index(request):
    return render(request, 'index.html')
def about_(request):
    return render(request, 'about.html')
def contact_(request):
    return render(request, 'contact.html')
def gallery_(request):
    return render(request, 'gallery.html')
def service_(request):
    return render(request,'services.html')
def sample_(request):
    product=Product.objects.all()
    context={}
    context['products']=product
    return render(request,'sample.html',context)
