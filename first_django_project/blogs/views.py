from django.shortcuts import HttpResponse, redirect, render
from django.http import JsonResponse


def root(request):
    return redirect("blogs/")


def index(request):
    context = {
        "name": "Gary",
        "favorite_color": "Orange",
        "kids": ["Avianna", "Gavin"]
    }
    return render(request, "index.html", context)


def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")


def create(request):
    return redirect("/")


def show(request, num):
    return HttpResponse('placeholder to display blog number: {}.' .format(num))


def edit(request, num):
    return HttpResponse('placeholder to edit blog number: {}.' .format(num))


def destroy(request, num):
    return redirect("/")


def bonus(request):
    return JsonResponse({"response": "JSON response from redirected_method", "status": True})
