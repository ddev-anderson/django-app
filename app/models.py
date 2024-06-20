from django.db import models

class Curso(models.Model):
    DIURNO = 'DIURNO'
    NOTURNO = 'NOTURNO'
    escolha_periodo = [
        (DIURNO, 'DIURNO'), (NOTURNO, 'NOTURNO')
    ]
    
    nome = models.CharField(max_length=30)
    descricao = models.CharField(max_length=300, default=None)
    periodo = models.CharField(max_length=20, choices=escolha_periodo, default=DIURNO)

    def __str__(self):
        return self.nome
