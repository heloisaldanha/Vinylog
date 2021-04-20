from django.db import models


class Tamanho(models.Model):
    tamanho = models.CharField(max_length=20)

    def __str__(self):
        return self.tamanho


class Vinil(models.Model):
    vinil = models.CharField(max_length=200)

    def __str__(self):
        return self.vinil


class Capa(models.Model):
    capa = models.CharField(max_length=200)

    def __str__(self):
        return self.capa


class Disco(models.Model):
    artista = models.CharField(max_length=200)
    album = models.CharField(max_length=200)
    pais = models.CharField(max_length=200, blank=True)
    lancamento = models.CharField(max_length=10, blank=True)
    gravadora = models.CharField(max_length=200, blank=True)
    cor = models.CharField(max_length=200, blank=True)
    tamanho = models.ForeignKey(Tamanho, on_delete=models.DO_NOTHING, blank=True)
    vinil = models.ForeignKey(Vinil, on_delete=models.DO_NOTHING, blank=True)
    capa = models.ForeignKey(Capa, on_delete=models.DO_NOTHING, blank=True)
    foto = models.ImageField(upload_to='pictures/%Y/%m')

    def __str__(self):
        return self.artista
