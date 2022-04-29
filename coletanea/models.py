from django.db import models

class Capa(models.Model):
    capa = models.FileField(upload_to='capas')

    def __str__(self) -> str:
        return self.arquivo.url

class Item(models.Model):
    tipo_choices = (('F', 'Filme'), ('S', 'Série'))

    categoria_choices = (('AC', 'Ação'), 
                        ('AV', 'Aventura'),
                        ('CM', 'Comédia'),
                        ('CMT', 'Comédia de Terror'),
                        ('CMA', 'Comédia de Ação'),
                        ('CMD', 'Comédia Tramádica'),
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
    
    titulo = models.TextField()
    resenha = models.TextField()
    tipo = models.CharField(max_length=2, choices=tipo_choices, default='F')
    categoria = models.CharField(max_length=4, choices=categoria_choices, default='AC')
    ano = models.DateField()
    temporadas = models.IntegerField()
    duracao = models.DurationField()
    rating = models.IntegerField()

    def __str__(self) -> str:
        return self.titulo
