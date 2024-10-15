from django.shortcuts import render
from django.views.generic.base import View
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy
from ReviewApp.forms import ReviewForm
from ReviewApp.models import Review
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm

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
            return HttpResponseRedirect(reverse_lazy("review:lista-review"))
        return None

def lista_review(request):
    if request.user.is_anonymous:
        return HttpResponseRedirect(reverse_lazy("login"))
    reviews = Review.objects.filter(user=request.user)
    return render(request, "lista_review.html", {"reviews": reviews})

def registro(request):
    if request.method == "POST":
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("home")
    else:
        formulario = UserCreationForm()
    context = {"form": formulario, }
    return render(request, "registration/registro.html", context)

class ReviewUpdateView(View):
    def get(self, request, pk, *args, **kwargs):
        review = Review.objects.get(pk=pk)
        formulario = ReviewForm(instance=review)
        context = {"formulario": formulario, }
        return render(request, "atualiza_review.html", context)

    def post(self, request, pk, *args, **kwargs):
        review: Review = get_object_or_404(Review, pk=pk)
        formulario = ReviewForm(request.POST, instance=review)
        if formulario.is_valid():
            review = formulario.save()  # cria uma review com os dados do formulário
            review.save()  # salva uma review no banco de dados
            return HttpResponseRedirect(reverse_lazy("review:lista-review"))
        contexto = {"formulario": formulario, }
        return render(request, "atualiza_review.html", contexto)

class ReviewDeleteView(View):
    def get(self, request, pk, *args, **kwargs):
        review = Review.objects.get(pk=pk)
        contexto = { "review": review, }
        return render(request, "deleta_review.html", contexto)

    def post(self, request, pk, *args, **kwargs):
        review = Review.objects.get(pk=pk)
        review.delete()
        return HttpResponseRedirect(reverse_lazy("review:lista-review"))