from django.contrib import admin
from django.urls import path
from.import views
urlpatterns = [
    path('up',views.index ,name='index'),
    path('',views.ftech ,name='ftech'),
    path('welcome',views.welcome ,name='wel')

]