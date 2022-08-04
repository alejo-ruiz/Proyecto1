from itertools import product
from multiprocessing import context
from django.shortcuts import render
from blog.models import Family

def create_family(request):
    new_family = Family.objects.create(name = "Eduardo", years = 55, last_name = "Simpson")
    
    new_family2 = Family.objects.create(name = "Laura", years = 56, last_name = "Simpson")
    
    new_family3 = Family.objects.create(name = "Emir", years = 21, last_name = "Simpson")
    
    context = {
        "new_family" :new_family,

        "new_family2" :new_family2,

        "new_family3" :new_family3

    }
    return render(request, "new_family.html", context=context)


def list_family(request):
    familys = Family.objects.all()
    context = {
        "familys":familys
    }
    return render(request, "list_family.html", context=context)
