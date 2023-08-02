from . import views
from django.urls import path



urlpatterns = [

    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('form/', views.form, name='form'),
    path('logout/', views.logout, name='logout'),
    path('refresh/', views.refresh, name='refresh'),
    path('msg/', views.msg, name='msg'),
    path('notify/',views.notify,name='notify'),

]
