from django.contrib import admin
from django.urls import path
from.import views
urlpatterns = [
    path('up',views.pati ,name='patient'),
    path('',views.pftech ,name='pftech'),
    path('pwelcome',views.pwelcome ,name='wel')

]