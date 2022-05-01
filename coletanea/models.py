from ast import Delete
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

class Item(models.Model):
    tipo_choices = (('F', 'Filme'), ('S', 'Série'))

    categoria_choices = (('AC', 'Ação'), 
                        ('AV', 'Aventura'),
                        ('CM', 'Comédia'),
                        ('CMT', 'Comédia de Terror'),
                        ('CMA', 'Comédia de Ação'),
                        ('CMD', 'Comédia Dramádica'),
                        ('CMR', 'Comédia Romântica'),
                        ('DA', 'Dança'),
                        ('DOC', 'Documentário'),
                        ('DOCF', 'Docuficção'),
                        ('DR', 'Drama'),
                        ('FA', 'Fantasia'),
                        ('FAC', 'Fantasia Científica'),
                        ('FC', 'Ficção Científica'),
                        ('FG', 'Filmes de Guerra'),
                        ('MI', 'Mistério'),
                        ('MU', 'Musical'),
                        ('FP', 'Filme Policial'),
                        ('RO', 'Romance'),
                        ('TE', 'Terror'),
                        ('TH', 'Thriller'),
                        )
    
    rating_stars = (1, 2, 3, 4, 5)
    
    user = models.ForeignKey(User, on_delete=Delete, null=True, blank=True)
    capa = models.ImageField(upload_to='capas/', null=True, blank=True)
    titulo = models.TextField()
    resenha = models.TextField()
    tipo = models.CharField(max_length=1, choices=tipo_choices, default='F')
    categoria = models.CharField(max_length=4, choices=categoria_choices, default='AC')
    ano = models.DateField()
    temporadas = models.IntegerField()
    duracao = models.DurationField()
    rating = models.IntegerField(default=0, 
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0),
        ]
    )

    def __str__(self) -> str:
        return self.titulo
