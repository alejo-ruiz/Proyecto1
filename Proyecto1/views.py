from django.http import HttpResponse
from django.shortcuts import render

def saludo(request):
    return HttpResponse("hola, es la base de datos")
def despedida(request):
    return HttpResponse("chau a la base de datos")

def template_con_lista(request):
    context = {
        "elemento_1" : "tomate",
        "elemento_1" : "tomate",
        "elemento_1" : "tomate"

    }

def template(request):
    context ={
        "name" : "alejo",
        "last_name" : "ruiz",
    }
    return render(request, "template1.html", context=context)

