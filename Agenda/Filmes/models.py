from django.db import models

# Create your models here.

class FilmeReview (models.Model):
    filme = models.CharField(max_length=100, help_text='Entre o nome do filme')
    review = models.CharField(max_length=500, help_text='Escreva sua review')
    nota = models.IntegerField(help_text='Qual nota você da?')