from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render,redirect,HttpResponse


def unauth(viewfunc):
    def wrapperfunc(request,*args, **kwargs):
        if request.user.is_authenticated:
          return redirect('system:Home')
        else:
            return viewfunc(request,*args,**kwargs)
    return wrapperfunc


def allowed_users(allowed_roles=[]):
    def decorator(viewfunc):
         def wrapperfunc(request,*args, **kwargs):
             group=None
             
             if request.user.groups.exists():
                 group=request.user.groups.all()[0].name
             if group in allowed_roles:
                 return viewfunc(request,*args,**kwargs) 
             else:
                 return HttpResponse('you are not allowed')
            
         return wrapperfunc
    return decorator
             



def admin_only(viewfunc):
    def wrapperfunc(request,*args, **kwargs):
        group=None
             
        if request.user.groups.exists():
            group=request.user.groups.all()[0].name

        if group =='admin':
            return viewfunc(request,*args,**kwargs) 
        if group =='patient':
            if request.path.startswith('/admin') or request.path.startswith('/medicalprovider/signup'):
                return redirect('Home:Home')
            else:
                return viewfunc(request,*args,**kwargs)
        if group =='doctors':
            if request.path.startswith('/admin') or request.path.startswith('/patientregister/signup'):
                return redirect('Home:Home')
            else:
                return viewfunc(request,*args,**kwargs)  
        else:
              return render(request,'Home/Home.html')    
           
    return wrapperfunc

