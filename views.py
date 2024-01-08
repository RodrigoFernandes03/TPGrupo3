from django.shortcuts import render
from django.db.models import Count
from django.views import View
from. models import bolos
from. forms import CustomerRegistrationForm

# Create your views here.
def home(request):
    return render(request,"home.html")

class CategoriaView(View):
    def get(self,request,val):
        id = bolos.objects.filter(categoria=val)
        titulo = bolos.objects.filter(categoria=val).values('titulo')
        return render(request,"categoria.html",locals())

class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationView()
        return render(request, 'customerregistration.html',locals())