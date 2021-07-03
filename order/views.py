from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from order.models import ShopCartForm, ShopCart


def index(request):
    return HttpResponse("Order App")

@login_required(login_url='/login')
def addtocart(request,id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = ShopCartForm(request.POST)
        if form.is_valid():
            current_user = request.user

            data = ShopCart()
            data.user_id = current_user.id
            data.service_id = id
            data.hour = form.cleaned_data['saat']
            data.save()

            messages.succes(request,"Hizmetimiz başarı ile sepete eklenmiştir.")
            return HttpResponseRedirect(url)