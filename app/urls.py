
from django.contrib import admin
from django.urls import path
from app import views





urlpatterns = [
    path('admin/', admin.site.urls),

 path('', views.home, name='home'),
path('contacts/', views.contacts, name='contacts'),
path('about/', views.about, name='about'),
path('show/', views.show, name='show'),
path('register/', views.register_view, name='register'),




]
