from django.shortcuts import render, redirect
from .models import Emprestimo
from livros.models import Livro
from usuarios.models import Usuario 

def emprestimo(request):
    if request.method == "POST":
        livro_id = request.POST.get('livro')
        usuario_id = request.POST.get('usuario')

        livro = Livro.objects.get(id=livro_id)
        usuario = Usuario.objects.get(id=usuario_id)

        Emprestimo.objects.create(
            livro=livro,
            usuario=usuario
        )
        return redirect('emprestimo')

    livros = Livro.objects.all()
    usuarios = Usuario.objects.all()
    return render(request, 'emprestimos.html', {
        'livros': livros,
        'usuarios': usuarios
    })