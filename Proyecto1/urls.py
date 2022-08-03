
from django.contrib import admin
from django.urls import path
from Proyecto1.views import despedida, saludo, template
from blog.views import create_family



urlpatterns = [
    path('admin/', admin.site.urls),
    path("saludo/", saludo),
    path("despedida/", despedida),
    path("template/", template),
    path("create_family/", create_family, name="create_family")
]
