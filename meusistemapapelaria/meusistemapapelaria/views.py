from urllib import request
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Itens, Colaborador, Cliente, ControleVendas
from .forms import ColaboradorForm, ClienteForm, ItensForm

# Pagina inicial

def pagina_inicial(request) :
    return render(request, 'meusistemapapelaria/pagina_inicial.html')

def cadastrar_colaborador(request):
    if request.method == 'POST':
        form = ColaboradorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Colaborador cadastrado com sucesso!')
            return redirect('cadastrar_colaborador')
        else:
       
         messages.error(request, 'Erro ao cadastrar colaborador. Verifique os dados e tente novamente.')
    else:      
        form = ColaboradorForm()
        
        return render(request, 'meusistemapapelaria/cadastrar_colaboradores.html', {'form': form})

def listar_colaboradores(request):
    colaboradores = Colaborador.objects.all()
    return render(request, 'meusistemapapelaria/listar_colaboradores.html', {'colaboradores': colaboradores})

def editar_colaborador(request, id):
    colaborador = get_object_or_404(Colaborador, id=id)
    if request.method == 'POST':
        form = ColaboradorForm(request.POST, instance=colaborador)
        if form.is_valid():
            form.save()
            messages.success(request, 'Colaborador atualizado com sucesso!')
            return redirect('listar_colaboradores')
        else:
            messages.error(request, 'Erro ao atualizar colaborador. Verifique os dados e tente novamente.')
    else:
        form = ColaboradorForm(instance=colaborador)
    return render(request, 'meusistemapapelaria/editar_colaboradores.html', {'form': form})

def excluir_colaborador(request, id):
    colaborador = get_object_or_404(Colaborador, id=id)
    if request.method == 'POST':
        colaborador.delete()
        messages.success(request, 'Colaborador excluído com sucesso!')
        return redirect('listar_colaboradores')