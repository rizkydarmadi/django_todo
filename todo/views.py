from django.http import HttpResponse
from django.template import loader
from .models import Todos
from django.shortcuts import render


def index(request):
    data = Todos.objects.all()
    context = {'data':data}
    return render(request,'index.html',context)