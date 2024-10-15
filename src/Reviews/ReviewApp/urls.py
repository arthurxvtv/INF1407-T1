"""
Created on 4 de out de 2024
@author: arthurxvtv
"""
from django.urls.conf import path
from ReviewApp import views

app_name = "review"

urlpatterns = [
    path("cria/", views.ReviewCreateView.as_view(), name="cria-review"),
    path("", views.lista_review, name="lista-review"),
    path("atualiza/<int:pk>/", views.ReviewUpdateView.as_view(), name="atualiza-review"),
    path("deleta/<int:pk>/", views.ReviewDeleteView.as_view(), name="deleta-review"),
]
