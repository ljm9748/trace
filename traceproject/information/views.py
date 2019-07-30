from django.shortcuts import render
from .models import Jikbang
from django.utils import timezone


def information(request):
    jikbang = Jikbang.objects
    return render(request,"information.html",{'jikbang':jikbang})

def newdata(request):
    return render(request, "newdata.html")

def create(hoho):
    blog = Jikbang()
    blog.title=hoho.GET['title']
    blog.title=hoho.GET['body']
    blog.pub_date=timezone.datetime.now()
    blog.save()
    return redirect('/blog/', +str(blog.id))
# Create your views here.
