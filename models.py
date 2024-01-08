from django.db import models

# Create your models here.

CATEGORY_CHOICES=(
    ('NL','Natal'),
    ('PT','Pastelaria'),
    ('PD','Padaria'),
    ('OB','Ovos Biológicos'),
    ('BT','Bolos e Tartes'),
)

class cliente (models.Model):
    id_customer = models.BigAutoField(primary_key=True)
    customer_name = models.CharField(max_length=100)
    customer_number = models.IntegerField()

def __str__(self):
    return str(self.customer_name)

class bolos (models.Model):
    id = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=150)
    preco = models.FloatField()
    descricao = models.TextField()
    categoria = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='product')
def __str__(self):
    return self.titulo

class funcionarios(models.Model):
    id_funcionarios = models.BigAutoField(primary_key=True)
    nome_funcionarios = models.CharField(max_length=150)
    funcao_funcionarios = models.CharField(max_length=200)
    
def __str__(self):
    return str (self.nome_funcionario)

class Vendas(models.Model):
    id_vendas = models.BigAutoField(primary_key=True)
    cliente = models.CharField(max_length=150)
    produto = models.CharField(max_length=150)
    quantidade = models.IntegerField()

def __str__(self):
    return str (self.cliente_vendas)
 
class Stock(models.Model):
    id_STOCK = models.BigAutoField(primary_key=True)
    Produto_Em_Stock = models.CharField(max_length=150)
    Quantidade_De_Produtos_Em_Stock = models.IntegerField(null=True),
    Quantidade_De_Produtos_Em_Falta_No_Stock = models.IntegerField(null=True),
    Quantidade_De_Produtos_Total_Que_Tem_De_Ter_Em_Stock = models.IntegerField(null=True),

def __str__(self):
    return str (self.Produto_Em_Stock)

class AvaliacaoProduto(models.Model):
    id_avaliacao = models.BigAutoField(primary_key=True)
    produto_avaliado = models.CharField(max_length=150)
    avaliacao = models.IntegerField()
    comentario = models.TextField(300)

    def __str__(self):
        return str (self.produto_avaliado)
    
class Despesas(models.Model):
    id_despesas = models.BigAutoField(primary_key=True)
    Nome_Despesa = models.CharField(max_length=150)
    Valor_Despesa = models.DecimalField(max_digits=10, decimal_places=2)
    Data_Despesa = models.DateField()

    def __str__(self):
        return str(self.Nome_Despesa)