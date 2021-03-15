from django.shortcuts import render, HttpResponse


def index(request):
    context = {
        "name" = "Gary",
        "favorite_color" = "orange",
        "kids" = ["Avianna", "Gavin"]
    }
    return render(request, "index.html")
