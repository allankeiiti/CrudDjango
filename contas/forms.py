from django.forms import ModelForm
from .models import Transacao, Categoria

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = ['tipo_categoria', 'nome_categoria']

class TransacaoForm(ModelForm):
    # Deve ser criado um Meta dentro do Form referente ao Model
    class Meta:
        model = Transacao
        fields = ['dt_transacao', 'descricao', 'valor', 'Categoria', 'observacoes']
