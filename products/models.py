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
    image = models.ImageField(upload_to='productos_img', null=True)
    priceUSD = models.DecimalField(max_digits=10, decimal_places=2)
    code = models.CharField(max_length=90)
    productCode = models.CharField(max_length=90)

    def __str__(self):
        return self.name

class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    valor_total = models.FloatField()
    telefono = models.CharField(max_length=20, blank=True, null=True)
    calle = models.CharField(max_length=60, null=True,blank=True)
    numero= models.CharField(max_length=40, null=True,blank=True)
    codigo_postal = models.CharField(max_length=50, null=True,blank=True)
    comentario = models.TextField(blank=True, null=True)
    correo= models.EmailField(blank=True,null=True)
    
class DetallePedido(models.Model):
    id_detalle_pedido = models.AutoField(primary_key=True)
    id_pedido = models.ForeignKey(Pedido, related_name='pedidos', on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Product, related_name='productos_pedidos', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.FloatField()
