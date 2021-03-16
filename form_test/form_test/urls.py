from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('form_app.routes')),

]
