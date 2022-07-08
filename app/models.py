from django.db import models

class dadosPessoal:
    primeiroNome = models.CharField(max_length=20)
    ultimoNome = models.CharField(max_length=20)
    nascimento = models.DateTimeField()

    

