from django.contrib import admin
from django.urls import include, path
from time_app import views

urlpatterns = [
    path('', include('time_app.routes')),

]
