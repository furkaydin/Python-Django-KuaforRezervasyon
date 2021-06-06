from unicodedata import category


import services as services
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from home.models import Setting,ContactFormu, ContactFormMessage
from service.models import Service, Images , Category


def index(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Service.objects.all()
    category=Category.objects.all()
    context = {'setting':setting,'category': category, 'page':'home','sliderdata':sliderdata}
    return render(request, 'index.html', context)

def hakkimizda(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Service.objects.all()
    context = {'setting':setting,'page':'hakkimizda','sliderdata':sliderdata}
    return render(request, 'hakkimizda.html', context)

def referanslar(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Service.objects.all()
    context = {'setting':setting,'page':'referanslar','sliderdata':sliderdata}
    return render(request, 'referanslarimiz.html', context)

def contact(request):
    if request.method == 'POST':
       form = ContactFormu(request.POST)
       if form.is_valid():
            data = ContactFormMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request , "Talebiniz başarılı bir şekilde gönderilmiştir. En kısa zamanda iletişime geçilecektir.")
            return HttpResponseRedirect ('/contact')

    setting = Setting.objects.get(pk=1)

    form = ContactFormu()
    sliderdata = Service.objects.all()
    context = {'setting': setting, 'form':form,'sliderdata':sliderdata}
    return render(request, 'contact.html', context)

def category_services(request,id,slug):
    category = Category.objects.all()
    categorydata = Category.objects.get(pk=id)
    services = Service.objects.filter(category_id=id)
    context = {'services':services,
               'category': category,
               'categorydata' : categorydata
               }
    return render(request,'services.html',context)

