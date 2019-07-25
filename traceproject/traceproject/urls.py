"""traceproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import main.views
import information.views
import gongu.views
import accounts.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',main.views.home,name='home'),
<<<<<<< HEAD
    path('information/', information.views.information, name='information'),
=======
<<<<<<< HEAD
    path('information/', information.views.information, name='information'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
=======
    path('information/', information.views.infortmation, name='information'),
>>>>>>> 066d49dc90f3d6a1455180d5c19f21a21c352436
    path('gongu/', gongu.views.gongu, name='gongu'),
    path('signup/', accounts.views.signup, name='signup'),
    path('login/', accounts.views.login, name='login'),

]
>>>>>>> 01a7984fe3b30bd5f6304a7cce061f9fee35c50b
