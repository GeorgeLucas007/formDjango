from django.db import models

class dadosPessoal(models.Model):
    primeiroNome = models.CharField('Nome', max_length=20)
    ultimoNome = models.CharField('Sobrenome', max_length=20)

    def __str__(self):
        return self.primeiroNome

