from django.shortcuts import render,redirect
from rest_framework import viewsets

from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'account created for {username}! Login to your account.')
            return redirect('login')
        else:
            messages.warning(request, f'please fill valid info!')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html',{'form':form})

#message.success
#message.warning
#message.info
#message.debug
#message.error

@login_required
def profile(request):
    return render(request, 'users/profile.html')


@login_required
def updateProfile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST , instance = request.user)            #user update instantiated
        p_form = ProfileUpdateForm(request.POST ,
                                    request.FILES ,
                                    instance = request.user.profile)         #user update instantiated

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'your profile has been updated.')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance = request.user)            #user update instantiated
        p_form = ProfileUpdateForm(instance = request.user.profile)         #user update instantiated
        context = {
            'u_form' : u_form,
            'p_form' : p_form
        }
    return render(request, 'users/updateProfile.html',context)
