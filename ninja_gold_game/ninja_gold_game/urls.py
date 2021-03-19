from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('', include('gold_app.routes')),
    path('process', include('gold_app.routes')),

]
