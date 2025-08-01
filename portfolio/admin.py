from django.contrib import admin
from .models import Projeto, Categoria

# Register your models here.

from django.contrib import admin
from .models import Projeto, Categoria

# Register your models here.

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'criado_em')
    search_fields = ('titulo', 'descricao')
    list_filter = ('categoria',)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
