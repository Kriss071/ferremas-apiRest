# Generated by Django 4.2.13 on 2024-05-30 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_image_alter_product_priceusd'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id_pedido', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('valor_total', models.FloatField()),
                ('telefono', models.CharField(blank=True, max_length=20, null=True)),
                ('calle', models.CharField(blank=True, max_length=60, null=True)),
                ('numero', models.CharField(blank=True, max_length=40, null=True)),
                ('codigo_postal', models.CharField(blank=True, max_length=50, null=True)),
                ('comentario', models.TextField(blank=True, null=True)),
                ('correo', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DetallePedido',
            fields=[
                ('id_detalle_pedido', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('precio_unitario', models.FloatField()),
                ('id_pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pedidos', to='products.pedido')),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productos_pedidos', to='products.product')),
            ],
        ),
    ]
