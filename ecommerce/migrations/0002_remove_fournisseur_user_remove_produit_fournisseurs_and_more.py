# Generated by Django 4.1 on 2022-08-12 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fournisseur',
            name='user',
        ),
        migrations.RemoveField(
            model_name='produit',
            name='fournisseurs',
        ),
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.DeleteModel(
            name='Fournisseur',
        ),
    ]
