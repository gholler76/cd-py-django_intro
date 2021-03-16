from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('', include('counter_app.routes')),
    path('/destroy', include('counter_app.routes')),

]
