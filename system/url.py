from django.urls import path,include
from . import views 
app_name='sytem'
urlpatterns = [
    path('',views.Home,name='Home'),
    # path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('sessions',views.sessions,name='sessions'),
    path('friends',views.friends,name='friends'),
    path('projects',views.projects,name='projects'),
    path('plans',views.plans,name='plans'),
    path('profile',views.profile,name='profile'),
    path('setting',views.setting,name='setting'),
    path('logout',views.logout,name='logout'),
    path('<int:pk>',views.delete_it,name='delete'),
    
]