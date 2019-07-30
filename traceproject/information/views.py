from django.shortcuts import render, redirect,     get_object_or_404
from .models import Jikbang
from django.utils import timezone

from .forms import Jikbang2



def information(request):
    jikbang = Jikbang.objects
    return render(request,"information.html",{'jikbang':jikbang})

def create(request):
    return render(request, "newdata.html")

def newdata(hoho):
    if hoho.method == 'POST' :
        form = Jikbang2(hoho.POST, hoho.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('home')
    else:
        form = Jikbang2()
        return render(hoho, 'newdata.html', {'form':form } )




    # blogs.title=hoho.GET['title']
    # blogs.title=hoho.GET['body']
    # blogs.save()
    # return redirect('/information/' + str(blogs.id))
# Create your views here.
