from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def advertisement_list(request, *args, **kwargs):
    return render(request, 'advertisement/advertisement_list.html', {})


def python_basic(request, *args, **kwargs):
    return render(request, 'advertisement/python_basic.html', {})


def django(request, *args, **kwargs):
    return render(request, 'advertisement/django.html', {})


def sql(request, *args, **kwargs):
    return render(request, 'advertisement/sql.html', {})


def web(request, *args, **kwargs):
    return render(request, 'advertisement/web.html', {})


def python_advanced(request, *args, **kwargs):
    return render(request, 'advertisement/python_advanced.html', {})