from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('', views.landing_page, name='home'),
    path('profile/', views.edit_profile, name='profile')
]
