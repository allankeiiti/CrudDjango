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
    return render(request, 'contas/form.html', data)
    # return render(request, 'contas/form.html', {'form':form})

    return render(request, 'contas/update.html', data)