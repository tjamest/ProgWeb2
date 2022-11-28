# Create your views here.

from django.shortcuts import render, get_object_or_404
from Filmes.models import FilmeReview
from django.views.generic.base import View
from Filmes.forms import FilmeReviewModel
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy


class FilmeList(View):
    def get(self, request, *args, **kwargs):
        reviews = FilmeReview.objects.all()
        context = { 'reviews': reviews, }
        return render(request,'Filmes/listaReview.html',context)

class FilmeReviewCreate(View):
    def get(self, request, *args, **kwargs):
        #retorna apenas 1 objeto, senão levanta uma excessão
        context = {'formulario': FilmeReviewModel}
        return render(request, 'Filmes/criaReview.html', context)

    def post(self, request, *args, **kwargs):
        formulario = FilmeReviewModel(request.POST)
        if formulario.is_valid():
            review = formulario.save()      #cria um objeto pessoa para o BD
            review.save()                  #cria um registro pessoa no BD
            return HttpResponseRedirect(reverse_lazy('Filmes:filme-review'))
        else:
            return render(request, 'Filmes/criaReview.html', {'formulario':formulario})


class FilmeReviewUpdate(View):
    def get(self, request, pk, *args, **kwargs):
        #retorna apenas 1 objeto, senão levanta uma excessão
        review = FilmeReview.objects.get(pk=pk)
        formulario = FilmeReviewModel(instance=review)
        context = {'review': formulario, }
        return render(request, 'Filmes/atualizaReview.html', context)

    def post(self, request, pk, *args, **kwargs):
        review = get_object_or_404(FilmeReview, pk=pk)
        formulario = FilmeReviewModel(request.POST, instance=review)
        if formulario.is_valid():
            review= formulario.save()	# cria uma pessoa com os dados do formulário
            review.save()									# salva uma pessoa no banco de dados
            return HttpResponseRedirect(reverse_lazy("Filmes:filme-review"))
        else:
            contexto = {'review': formulario, }
            return render(request, 'Filmes/atualizaReview.html', contexto)
            

class FilmeReviewDelete(View):
    def get(self, request, pk, *args, **kwargs):
        review = FilmeReview.objects.get(pk=pk)
        contexto = { 'review': review, }
        return render(
            request, 'Filmes/apagaReview.html', 
              contexto)

    def post(self, request, pk, *args, **kwargs):
        review = FilmeReview.objects.get(pk=pk)
        review.delete()
        return HttpResponseRedirect(
            reverse_lazy("Filmes:filme-review"))