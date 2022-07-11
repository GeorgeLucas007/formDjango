from django.contrib import admin
from .models import *

class PessoaAdmin(admin.ModelAdmin):
    list_display = ('primeiroNome', 'ultimoNome')

admin.site.register(dadosPessoal, PessoaAdmin)
