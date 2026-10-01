from django.shortcuts import render, redirect
from .models import Livro

def livros(request):
    if request.method == "POST":
        titulo = request.POST.get('titulo')
        autor = request.POST.get('autor')
        isbn = request.POST.get('isbn')
        ano_publicacao = request.POST.get('ano_publicacao')

        Livro.objects.create(
            titulo=titulo,
            autor=autor,
            isbn=isbn,
            ano_publicacao=ano_publicacao
        )
        return redirect('livros')
    
    lista_livros = Livro.objects.all().order_by('-data_cadastro')
    return render(request, 'livros.html', {'livros': lista_livros})