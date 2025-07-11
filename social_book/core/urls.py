from django.urls import path
from . import views

urlpatterns = [

    path('',views.index, name='index'),
    path('signup',views.signup, name='signup'),
    path('upload',views.upload, name='upload'),
    path('signin',views.signin, name='signin'),
    path('testing',views.testing, name='testing'),
    path('logout',views.logout, name='logout'),
    path('settings',views.settings, name='settings')
]