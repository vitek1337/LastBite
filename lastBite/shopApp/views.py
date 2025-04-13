from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.context_processors import request

from .models import Goods


def index(request):
    products = Goods.objects.all()
    return render(request, "index.html", {"products": products})