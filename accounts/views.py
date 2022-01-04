from django.shortcuts import get_object_or_404, render, redirect
from .forms import  UserForm
from .models import Account
from Purchase.models import *
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Account activation 
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
import requests


# Create your views here.

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(request, email=email, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are now logged in!")
            return redirect('home')
            
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')
    return render(request, 'Accounts/login.html')

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request, "You are logged out!")
    return redirect('login')

@login_required(login_url='login')
def dashboard(request):
    userprofile = request.user
    context = {
        'userprofile': userprofile,
    }
    return render(request, 'Accounts/user_profile.html', context)

@login_required(login_url='login')
def edit_profile(request):
    
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user) # using instance because we want to update the profile 
        if user_form.is_valid() :
            user_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('edit_profile')
    else:
        user_form = UserForm(instance=request.user)
    context = {
        'user_form': user_form,
       
    }
    return render(request, 'Accounts/edit_profile.html', context)

def forgotPassword(request):
    if request.method == 'POST':
        email = request.POST['email']
        if Account.objects.filter(email=email).exists():
            user = Account.objects.get(email__exact=email)

            # Reset password email
            current_site = get_current_site(request)
            mail_subject = 'Reset your password'
            message = render_to_string('Accounts/reset_password_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = email
            send_mail = EmailMessage(mail_subject, message, to=[to_email])
            send_mail.send()
            messages.success(request, "Password reset email has been sent to your email address.")
            return redirect('login')
        
        else:
            messages.error(request, "Account does not exist!")
            return redirect('forgotPassword')
    return render(request, 'Accounts/forgotPassword.html')

def resetpassword_validate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None
    
    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.success(request, "Please reset your password")
        return redirect('resetPassword')
    else:
        messages.error(request, 'This link has been expired!')
        return redirect('login')

def resetPassword(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            uid = request.session.get('uid')
            user = Account.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request, 'Password reset successful.')
            return redirect('login')
        else:
            messages.error(request, "Password does not match!")
            return redirect('resetPassword')
    else:
        return render(request, 'Accounts/resetPassword.html')


@login_required(login_url='login')
def change_password(request):
    if request.method == 'POST':
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']

        user = Account.objects.get(username__exact=request.user.username)

        if new_password == confirm_password:
            success = user.check_password(current_password)
            if success:
                user.set_password(new_password)
                user.save()
                # auth.logout(request) for log out after change password
                messages.success(request, 'Password updated successfully.')
                return redirect('change_password')
            else:
                messages.error(request, 'Please enter valid current password.')
                return redirect('change_password')
        else:
            messages.error(request, 'Password does not match!')
            return redirect('change_password')

    return render(request, 'Accounts/change_password.html')

