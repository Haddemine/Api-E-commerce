# Generated by Django 4.1 on 2022-08-16 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0002_commande_commandeitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='prix',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
