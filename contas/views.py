from django.shortcuts import render, redirect
# from django.http import HttpResponse
from contas.models import Transacao, Categoria
from .forms import TransacaoForm, CategoriaForm
import datetime

def home(request):

    data = {}
    data['transacoes'] = ['t1', 't2', 't3']

    data['now'] = datetime.datetime.now()
    # html = '<html><title>DateTime</title><body>Agora é %s.</body></html>' % now
    # return HttpResponse(html)
    return render(request, 'contas/home.html', data)

def listagem(request):
    data = {}
    data['transacoes'] = Transacao.objects.all()
    data['categorias'] = Categoria.objects.all()
    return render(request, 'contas/listagem.html', data)

def nova_transacao(request):
    data = {}
    form = TransacaoForm(request.POST or None)

    # Validar o Form
    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    data['form'] = form
    return render(request, 'contas/form.html', data)
    # return render(request, 'contas/form.html', {'form':form})

def update(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    data = {}
    form = TransacaoForm(request.POST or None, instance=transacao)

    # Validar o Form
    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    data['form'] = form
    data['transacao'] = transacao
    return render(request, 'contas/form.html', data)
    # return render(request, 'contas/form.html', {'form':form})

def delete(pk):
    transacao = TransacaoForm.objetcs.get(pk=pk)
    transacao.delete()
    return redirect('url_listagem')

# Categoria
def nova_categoria(request):
    data = {}
    form = CategoriaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    data['form'] = form
    return render(request, 'contas/form_categoria.html', data)

def update_categoria(request, pk):
    categoria = Categoria.objects.get(pk=pk)
    data = {}
    form = CategoriaForm(request.POST or None, instance=categoria)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    data['form'] = form
    data['categoria'] = categoria
    return render(request, 'contas/form_categoria.html', data)


def delete_categoria(pk):
    categoria = CategoriaForm.objects.get(pk=pk)
    categoria.delete()
    return redirect('url_listagem')