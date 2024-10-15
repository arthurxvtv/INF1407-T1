"""
URL configuration for Reviews project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.views import PasswordChangeDoneView
from django.urls import path
from django.urls.base import reverse_lazy
from django.urls.conf import include
from ReviewApp.views import home, registro

urlpatterns = [
    path("admin/", admin.site.urls),
    # incluir a seguinte linha
    path("login/", LoginView.as_view(template_name="registration/login.html",), name="login"),
    path("", home, name="home"),
    path("logout/", LogoutView.as_view(next_page=reverse_lazy("home"),), name="logout"),
    path("review/", include("ReviewApp.urls")),
    path("registro/", registro, name="registro"),
    path("alterar-senha/", PasswordChangeView.as_view(template_name="registration/alterar_senha.html", success_url=reverse_lazy("alterar_senha_sucesso")), name="alterar_senha"),
    path("alterar-senha/done/", PasswordChangeDoneView.as_view(template_name="registration/alterar_senha_sucesso.html",), name="alterar_senha_sucesso"),
]
