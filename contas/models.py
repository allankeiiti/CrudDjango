from django.db import models

class Categoria(models.Model):
    tipo_categoria = models.IntegerField(primary_key = True)
    nome_categoria = models.CharField(max_length = 100)
    dt_criacao = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.nome_categoria

class Transacao(models.Model):
    dt_transacao = models.DateTimeField()
    descricao = models.CharField(max_length = 200)
    valor = models.DecimalField(max_digits = 7, decimal_places = 2)
    Categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    observacoes = models.TextField(null = True, blank = True)

    # Alterando como fica o display da classe nos Fields
    class Meta:
        verbose_name_plural = 'Transações'

    def __str__(self):
        return self.descricao