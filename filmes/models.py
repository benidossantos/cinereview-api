from django.db import models

class Filme(models.Model):

    GENERO_CHOICES = [
        ('ACAO', 'Ação'),
        ('DRAMA', 'Drama'),
        ('COMEDIA', 'Comédia'),
        ('TERROR', 'Terror'),
        ('FICCAO', 'Ficção Científica'),
    ]

    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    genero = models.CharField(max_length=20, choices=GENERO_CHOICES)
    ano_lancamento = models.IntegerField()

    def __str__(self):
        return self.titulo


class Avaliacao(models.Model):

    NOTA_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    filme = models.ForeignKey(Filme, on_delete=models.CASCADE)
    nota = models.IntegerField(choices=NOTA_CHOICES)
    comentario = models.TextField()
    data_avaliacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.filme.titulo} - {self.nota}"
