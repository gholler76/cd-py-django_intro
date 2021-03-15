from django.shortcuts import HttpResponse, redirect, render
from django.http import JsonResponse
from time import gmtime, strftime


def index(request):
    context = {
        "date": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request, "index.html", context)
