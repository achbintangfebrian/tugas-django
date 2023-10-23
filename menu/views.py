from django.http import HttpResponse
from django.template import loader


# Create your views here.

def beranda(request):
    template = loader.get_template("beranda.html")
    return HttpResponse(template.render())


def kelas(request):
    template = loader.get_template("kelas.html")
    return HttpResponse(template.render())

def jadwal(request):
    template = loader.get_template("jadwal.html")
    return HttpResponse(template.render())    

   