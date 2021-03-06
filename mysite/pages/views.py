from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    home_context = {
        "nav": "home"
    }
    return render(request, "home.html", home_context)

def find_event_view(request, *args, **kwargs):
    find_event_context = {
        "nav" : "find_event"
    }
    return render(request, "find_event.html", find_event_context)

def create_event_view(request, *args, **kwargs):
    create_event_context = {
        "nav" : "create_event"
    }
    return render(request, "create_event.html", create_event_context)

def contact_view(request, *args, **kwargs):
    contact_context = {
        "nav" : "contact"
    }
    return render(request, "contact.html", contact_context)

def login_view(request, *args, **kwargs):
    login_context = {
        "nav" : "login"
    }
    return render(request, "login.html", login_context)

def sign_up_view(request, *args, **kwargs):
    sign_up_context = {
        "nav" : "sign_up"
    }
    return render(request, "sign_up.html", sign_up_context)

def personal_view(request, *args, **kwargs):
    personal_context ={
        "nav":"login"
    }
    return render(request,"personal.html",personal_context)