from itertools import product
from multiprocessing import context
from django.shortcuts import render
from blog.models import Family

def create_family(request):
    new_family = Family.objects.create(name = "Eduardo", years = 55)
    context = {
        "new_family" :new_family
    }
    return render(request, "new_family.html", context=context)
    