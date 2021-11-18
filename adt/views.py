from django.shortcuts import render
from django.template import loader
from .models import Adt


# Create your views here.
def index(request):
    bbs = Adt.objects.all()
    return render(request, 'adt/index.html', {'bbs': bbs})
