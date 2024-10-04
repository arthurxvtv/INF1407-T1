"""
Created on 4 de out de 2024
@author: tutuzinsheik
"""
from django.urls.conf import path
from ReviewApp import views

app_name = "review"

urlpatterns = [
    path("cria/", views.ReviewCreateView.as_view(), name="cria-review"),
    # path("lista/", views.ContatoListView.as_view(), name="lista-contatos"),
    # path("", views.ContatoListView.as_view(), name="home-contatos"),
]
