from django.db import models

# Create your models here.


class Filmes(models.Model):
    nome = models.CharField(max_length=55)
    categoria_id = models.BigIntegerField()

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=55)

    def __str__(self):
        return self.nome

class Assinatura(models.Model):
    nome = models.CharField(max_length=55)
    valor = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return self.nome

class Usuarios(models.Model):
    nome = models.CharField(max_length=55)
    valor = models.DecimalField(max_digits=9,decimal_places=2)
    assinatura_fk = models.BigIntegerField()

    def __str__(self):
        return self.nome
    
class Favoritos(models.Model):
    filme_id = models.BigIntegerField()
    usuarios_id = models.BigIntegerField()
    