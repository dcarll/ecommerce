from django.db import models

# Create your models here.
class Produto(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = "Produtos"
