from django.shortcuts import HttpResponse, redirect, render
from django.http import JsonResponse


def index(request):
    return render(request, "index.html")


def create_user(request):
    print("Got POST Info................................")
    post_name = request.POST['form_name']
    post_instructor = request.POST['form_instructor']
    post_stack_radio = request.POST['form_stack_radio']
    post_opp_checkbox = request.POST['form_opp_checkbox.value']
    context = {
        "result_name": post_name,
        "result_instr": post_instructor,
        "result_stack": post_stack_radio,
        "result_opp": post_opp_checkbox
    }
    return render(request, "result.html", context)
