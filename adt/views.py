from django.shortcuts import render
from django.template import loader
from .models import Adt, Rubric


# Create your views here.
def index(request):
    bbs = Adt.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs':bbs,'rubrics': rubrics}
    return render(request, 'adt/index.html', context)


def by_rubric(request, rubric_id):
    bbs = Adt.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs': bbs, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, 'adt/by_rubric.html', context)
