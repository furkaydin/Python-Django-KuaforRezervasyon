
from django.contrib import messages

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from home.models import UserProfile, Setting
from reserve.models import Reserve
from service.models import Category, Comment
from user.forms import UserUpdateForm, ProfileUpdateForm


def index(request):
    category=Category.objects.all()
    current_user = request.user

    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {'category':category,
               'profile':profile,
               }
    return render(request,'user_profile.html',context)

@login_required(login_url='/login')
def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('/user')


    else:
            category = Category.objects.all()
            user_form = UserUpdateForm(instance=request.user)
            profile_form = ProfileUpdateForm(instance=request.user.userprofile)
            context = {
                'category': category,
                'user_form': user_form,
                'profile_form': profile_form,
            }
            return render(request, 'user_update.html', context)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request,'Şifreniz başarı ile değiştirilmiştir.')
            return redirect('/user')
        else:
            messages.error(request,'Lütfen gerekli düzenlemeleri yapınız.'+ str(form.errors))
            return HttpResponseRedirect('/user/password')
    else:
        category = Category.objects.all()
        form = PasswordChangeForm(request.user)
        return render(request, 'change_password.html', {
            'form':form,'category':category
        })


@login_required(login_url="/login")
def reserve(request):
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    current_user = request.user
    reserve = Reserve.objects.filter(user_id=current_user.id)

    context = {
        'category': category,
        'reserve': reserve,
        'setting': setting,
    }
    return render(request, 'user_reserve.html', context)

@login_required(login_url="/login")
def deletereserve(request,id):
    current_user = request.user
    Reserve.objects.filter(id=id, user_id=current_user.id).delete()
    messages.success(request, 'Randevu İptal Edildi')
    return HttpResponseRedirect('/user/reserve')


@login_required(login_url="/login")
def user_comments(request):
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    current_user = request.user
    comments = Comment.objects.filter(user_id=current_user.id)
    context = {
        'category': category,
        'comments': comments,
        'setting':setting,
    }
    return render(request, 'user_comments.html', context)

@login_required(login_url='/login') # Check login
def user_deletecomment(request,id):
    current_user = request.user
    Comment.objects.filter(id=id, user_id=current_user.id).delete()
    messages.success(request, 'Comment deleted..')
    return HttpResponseRedirect('/user/comments')