from django.db import models

# Create your models here.
class Genero(models.Model):
    descricao = models.CharField(max_length=50, verbose_name="Descrição")

    def __str__(self):
        return self.descricao

