from django.shortcuts import render
from django.views.generic.base import View
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy
from ReviewApp.forms import ReviewForm

# Create your views here.
def home(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    return render(request, "home.html")

class ReviewCreateView(View):
    def get(self, request, *args, **kwargs):
        contexto = { 'formulario': ReviewForm, }
        return render(request, "cria_review.html", contexto)

    def post(self, request, *args, **kwargs):
        formulario = ReviewForm(request.POST)
        if formulario.is_valid():
            contato = formulario.save()
            contato.save()
            return HttpResponseRedirect(reverse_lazy("contatos:lista-contatos"))
        return None
