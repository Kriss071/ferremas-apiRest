from django.db import models

# Create your models here.

class Categoria(models.Model):
    name = models.CharField(max_length=90)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=90)
    id_categoria = models.ForeignKey(Categoria, related_name='productos_categorias', on_delete=models.SET_NULL, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    marca = models.CharField(blank=True, null=True, max_length=50)
    image = models.ImageField(upload_to='productos', null=True)
    priceUSD = models.IntegerField()
    code = models.CharField(max_length=90)
    productCode = models.CharField(max_length=90)

    def __str__(self):
        return self.name

