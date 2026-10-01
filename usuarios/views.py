from django.shortcuts import render, redirect
from .models import Usuario

def usuarios(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')

        Usuario.objects.create(
            nome=nome,
            email=email,
            telefone=telefone
        )
        return redirect('usuarios')

    return render(request, 'usuarios.html')