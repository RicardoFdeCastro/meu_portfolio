from django.shortcuts import render
from .models import Projeto, Categoria
# Create your views here.


def home(request):
    projetos = Projeto.objects.all()
    return render(request, 'portfolio/home.html', {'projetos': projetos})



def home(request):
    categoria_id = request.GET.get('categoria')
    categorias = Categoria.objects.all()

    if categoria_id:
        projetos = Projeto.objects.filter(categoria_id=categoria_id)
    else:
        projetos = Projeto.objects.all()

    return render(request, 'portfolio/home.html', {
        'projetos': projetos,
        'categorias': categorias,
        'categoria_selecionada': categoria_id,
    })
