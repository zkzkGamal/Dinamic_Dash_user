from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from .decorators import unauth, allowed_users, admin_only
from django.urls import reverse
from .models import *
from django.contrib import messages
from django.contrib import auth
from .decorators import *
# Done


def check_token(request, username, email, password, confirmpassword):
   # to check the usr is token or
    if User.objects.filter(username=username).exists():
        error_message = 'Username already taken'
        messages.error(request, error_message)
        return error_message

    if User.objects.filter(email=email).exists():
        error_message = 'Email already registered'
        messages.error(request, error_message)
        return error_message

    if password != confirmpassword:
        error_message = 'Passwords do not match'
        messages.error(request, error_message)
        return error_message
# Done


def redirect_with_delay(request, url, delay_seconds=20000, error_message=None):
    if error_message:
        messages.error(request, error_message)
    response = redirect(url)
    response['Refresh'] = delay_seconds
    return response
# Done


@unauth
def signup(request):
    if request.method == 'POST':
        log = request.POST.get('login')
        sign = request.POST.get('signup')
        if log:
            password = request.POST.get('Pass1word')
            username = request.POST.get('UserName')
            user1 = auth.authenticate(
                request, username=username, password=password)
            if user1 is not None:
                auth.login(request, user1)
                next_url = request.GET.get('next')
                if next_url == '' or next_url == None:
                    next_url = 'system:Home'
                return redirect('system:Home')
            else:
                messages.error(request, 'please check username or password')
        else:
            password = request.POST.get('Password')
            email = request.POST.get('Email Address')
            confirmpassword = request.POST.get('Repeat Password')
            username = request.POST.get('Username')
            checked = check_token(request, username, email,
                                  password, confirmpassword)
            if checked:
                return redirect_with_delay(request, reverse('system:signup'), error_message=checked)
            else:
                user = User.objects.create_user(username, email, password)
                data = account(
                    username=username,
                    email=email,
                    password=password,
                    user=user,
                )
                group = Group.objects.get(name='user')
                user.groups.add(group)
                data.save()
                user.save()
                return redirect('system:Home')
    else:
        return render(request, 'login-register.html')
# @admin_only
# Done


@login_required(login_url='system:signup')
def Home(request):
    account1 = account.objects.get(user=request.user)
    if request.method == 'POST':
        title = request.POST.get('title')
        thought = request.POST.get('thought')
        draf = draft(title=title, thought=thought, user=request.user)
        if draf is not None:
            draf.save()
            return redirect('system:Home')
    drafs = draft.objects.filter(user=request.user)
    return render(request, 'index.html', {'draf': drafs, 'acc': account1})
# Done


@login_required(login_url='system:signup')
def profile(request):
    user1 = request.user.groups.filter(name='user').exists()
    Account = account.objects.get(user=request.user)
    if request.method == 'POST':
        if request.POST.get('profilePic'):
            account1 = account.objects.get(user=request.user)
            proPic = request.FILES.get('profileImg')
            account1.proPic = proPic
            if request.method == 'POST':
                account1.save()
        else:
            fullname = request.POST.get('fullName')
            gender = request.POST.get('gender')
            country = request.POST.get('country')
            phone = request.POST.get('phone')
            DateOfBirth = request.POST.get('date')
            DocOrPat = request.POST.get('docOrPatient')
            specialList = request.POST.get('spacial')
            yearOfExp = request.POST.get('YearsOfExp')
            payMethod = request.POST.get('PayMethod')
            payEmail = request.POST.get('Payemail')
            proPic = request.FILES.get('profileImg')
            price = request.POST.get('price')

            account1 = account.objects.get(user=request.user)
            account1.fullName = fullname
            account1.gender = gender
            account1.country = country
            account1.phone = phone
            account1.DateOfBirth = DateOfBirth
            account1.DocOrPat = DocOrPat
            account1.specialList = specialList
            account1.yearOfExp = yearOfExp
            account1.payMethod = payMethod
            account1.payEmail = payEmail
            account1.price = price
            account1.save()
            if DocOrPat == 'doctor':
                group = Group.objects.get(name='doctor')
                user = Group.objects.get(name='user')
                request.user.groups.add(group)
                request.user.groups.remove(user)
            else:
                group = Group.objects.get(name='patient')
                user = Group.objects.get(name='user')
                request.user.groups.add(group)
                request.user.groups.remove(user)
    return render(request, 'profile.html', {'user1': user1, 'account': Account})
# Done


def logout(request):
    auth.logout(request)
    return redirect('system:signup')
# done


def delete_it(request, pk):
    obj = draft.objects.get(id=pk)
    obj.delete()
    return redirect('system:Home')


def sessions(request):
    doctors = account.objects.filter(DocOrPat='doctor')
    return render(request, 'doctors.html', {'doctors': doctors})


def friends(request):
    return render(request, 'friends.html')


def plans(request):
    return render(request, 'plans.html')


def projects(request):
    return render(request, 'projects.html')


def setting(request):
    return render(request, 'settings.html')
