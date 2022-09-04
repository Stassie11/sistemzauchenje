"""sistemzauchenje URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin

from django.urls import path
from django.views.static import serve

from italian import views
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('index.html', views.index, name="index"),
    path('contact.html', views.contact, name="contact"),
    path('entertainment.html', views.entertainment, name="entertainment"),
    path('first.html', views.first, name="first"),
    path('second.html', views.second, name="second"),
    path('third.html', views.third, name="third"),
    path('start.html', views.start, name="start"),
    path('lectures.html', views.lectures, name="lectures"),
    path('test.html', views.test, name="test"),
    path("signup.html", views.register_request, name="signup"),
    path("login.html", views.login_request, name="login"),
    path("logout.html", views.logout_request, name="logout"),
    path("quiz.html", views.quiz, name="quiz"),

]
