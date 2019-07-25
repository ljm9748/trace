from django.shortcuts import render
from .models import Jikbang

<<<<<<< HEAD
def information(request) :
    return render(request,"information.html")
=======
def information(request):
    jikbang = Jikbang.objects
    return render(request,"information.html",{'jikbang':jikbang})
>>>>>>> 066d49dc90f3d6a1455180d5c19f21a21c352436
# Create your views here.
