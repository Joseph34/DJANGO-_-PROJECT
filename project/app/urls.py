from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('announcement', views.Announcement, name='Announcement'),
    path('announcedet', views.Announcedet, name='Announcement-details'),
    
]