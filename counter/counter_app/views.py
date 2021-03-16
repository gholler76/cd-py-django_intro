from django.shortcuts import HttpResponse, redirect, render
from django.db import models


def index(request):

    if "counter" not in request.session:
        request.session['counter'] = 1
    else:
        request.session['counter'] += 1

    counter = request.session['counter']

    context = {
        'view_counter': counter
    }
    return render(request, 'index.html', context)


def destroy(request):
    del request.session['counter']
    return redirect('/')
