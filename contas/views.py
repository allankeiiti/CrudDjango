from django.shortcuts import render
# from django.http import HttpResponse
import datetime
from contas.models import Transacao, Categoria

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
