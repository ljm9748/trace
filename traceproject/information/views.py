from django.shortcuts import render
from .models import Jikbang

def information(request):
    jikbang = Jikbang.objects
    return render(request,"information.html",{'jikbang':jikbang})
# Create your views here.
