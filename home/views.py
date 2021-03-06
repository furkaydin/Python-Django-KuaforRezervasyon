from unicodedata import category


import services as services
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from home.form import SignUpForm
from home.models import Setting, ContactFormu, ContactFormMessage, UserProfile, FAQ
from service.models import Service, Images, Category, Comment, Barber


def index(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Service.objects.all()
    category=Category.objects.all()
    ourblog = Service.objects.all().order_by('?')[:3]
    about = Service.objects.all().order_by('id')[:5]
    context = {'setting':setting,'category': category, 'page':'home','sliderdata':sliderdata, 'ourblog' : ourblog , 'about' : about}
    return render(request, 'index.html', context)

def hakkimizda(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Service.objects.all()
    category = Category.objects.all()
    context = {'setting':setting,'page':'hakkimizda','sliderdata':sliderdata , 'category':category}
    return render(request, 'hakkimizda.html', context)

def referanslar(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Service.objects.all()
    category = Category.objects.all()
    context = {'setting':setting,'page':'referanslar','sliderdata':sliderdata, 'category':category}
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
    category = Category.objects.all()
    form = ContactFormu()
    sliderdata = Service.objects.all()
    context = {'setting': setting, 'form':form,'sliderdata':sliderdata , 'category':category}
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

def service_detail(request,id,slug):
    category = Category.objects.all()
    service = Service.objects.get(pk=id)
    images = Images.objects.filter(service_id=id)
    barber = Barber.objects.all()
    comments = Comment.objects.filter(service_id=id,status='True')
    context = {'service': service,
               'category': category,
               'images': images,
               'comments': comments,
               'barber':barber,
           }
    return render(request,'service_detail.html',context)

def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect('/')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        return HttpResponseRedirect('/')



    category = Category.objects.all()
    context = {'category': category,

               }
    return render(request, 'login.html', context)



def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            current_user = request.user
            data =UserProfile()
            data.user_id=current_user.id
            data.image="images/users/user.png"
            data.save()
            messages.success(request,"Sitemize başarılı bir şekilde üye oldunuz.")
        return HttpResponseRedirect('/')

    form = SignUpForm
    category = Category.objects.all()
    context = {'category': category,
               'form': form,

                   }
    return render(request, 'signup.html', context)


def faq(request):
    category = Category.objects.all()
    faq = FAQ.objects.all()
    setting = Setting.objects.get(pk=1)


    context = {
        'faq': faq,
        'category':category,
        'setting':setting,

    }
    return render(request, 'faq.html', context)