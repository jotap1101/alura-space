from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from apps.galeria.forms import FotografiaForm
from apps.galeria.models import Fotografia

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Você precisa estar logado para acessar essa página!')

        return redirect('login')

    fotografias = Fotografia.objects.all().filter(status=True).order_by('data_fotografia')

    context = {
        'fotografias': fotografias
    }

    return render(request, 'galeria/index.html', context)

def imagem(request, id):
    fotografia = get_object_or_404(Fotografia, pk=id)

    context = {
        'fotografia': fotografia
    }

    return render(request, 'galeria/imagem.html', context)

def search(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Você precisa estar logado para acessar essa página!')

        return redirect('login')

    fotografias = Fotografia.objects.all().filter(status=True).order_by('data_fotografia')

    if 'search' in request.GET:
        search = request.GET['search']
        
        if search:
            fotografias = fotografias.filter(nome__icontains=search)

    context = {
        'fotografias': fotografias
    }

    return render(request, 'galeria/index.html', context)

def filter(request, categoria):
    if not request.user.is_authenticated:
        messages.error(request, 'Você precisa estar logado para acessar essa página!')

        return redirect('login')

    fotografias = Fotografia.objects.all().filter(status=True, categoria=categoria).order_by('data_fotografia')

    context = {
        'fotografias': fotografias
    }

    return render(request, 'galeria/index.html', context)

def criar_fotografia(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Você precisa estar logado para acessar essa página!')

        return redirect('login')

    form = FotografiaForm()

    if request.method == 'POST':
        form = FotografiaForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            messages.success(request, 'Fotografia criada com sucesso!')

            return redirect('index')
        
        messages.error(request, 'Erro ao criar a fotografia!')

    context = {
        'form': form
    }

    return render(request, 'galeria/criar_fotografia.html', context)

def editar_fotografia(request, id):
    if not request.user.is_authenticated:
        messages.error(request, 'Você precisa estar logado para acessar essa página!')

        return redirect('login')

    fotografia = Fotografia.objects.get(id=id)
    form = FotografiaForm(instance=fotografia)

    if request.method == 'POST':
        form = FotografiaForm(request.POST, request.FILES, instance=fotografia)

        if form.is_valid():
            form.save()

            messages.success(request, 'Fotografia editada com sucesso!')

            return redirect('index')
        
        messages.error(request, 'Erro ao editar a fotografia!')

    context = {
        'form': form,
        'id': id
    }

    return render(request, 'galeria/editar_fotografia.html', context)

def excluir_fotografia(request, id):
    if not request.user.is_authenticated:
        messages.error(request, 'Você precisa estar logado para acessar essa página!')

        return redirect('login')

    fotografia = Fotografia.objects.get(id=id)

    fotografia.delete()

    messages.success(request, 'Fotografia excluída com sucesso!')

    return redirect('index')