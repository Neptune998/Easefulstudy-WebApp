from django.shortcuts import render
from django.http import HttpResponse


def homepage(request):
    return render(request=request,
                  template_name='Easefulstudy_template/home.html')


def about(request):
    return render(request=request,
                  template_name='Easefulstudy_template/about.html')


