# Generated by Django 4.2.13 on 2024-05-23 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90)),
                ('description', models.TextField(blank=True, null=True)),
                ('marca', models.CharField(blank=True, max_length=50, null=True)),
                ('image', models.ImageField(null=True, upload_to='productos')),
                ('priceUSD', models.IntegerField()),
                ('code', models.CharField(max_length=90)),
                ('productCode', models.CharField(max_length=90)),
                ('id_categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='productos_categorias', to='products.categoria')),
            ],
        ),
    ]
