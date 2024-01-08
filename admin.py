from django.contrib import admin
from .models import cliente
admin.site.register(cliente)
from django.contrib import admin
from .models import funcionarios
admin.site.register(funcionarios)
from django.contrib import admin
from .models import Vendas
admin.site.register(Vendas)
from .models import Stock
admin.site.register(Stock)
from .models import AvaliacaoProduto   
admin.site.register(AvaliacaoProduto)
from .models import Despesas 
admin.site.register(Despesas)
# Register your models here.

from .models import bolos
admin.site.register(bolos)
class bolosModelAdmin(admin.ModelAdmin):
    list_display = ['id','titulo','preco','descricao','categoria','product_image']