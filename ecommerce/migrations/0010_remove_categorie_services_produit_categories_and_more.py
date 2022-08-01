# Generated by Django 4.0.6 on 2022-07-30 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0009_produit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorie',
            name='services',
        ),
        migrations.AddField(
            model_name='produit',
            name='categories',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecommerce.categorie'),
        ),
        migrations.AlterField(
            model_name='produit',
            name='image',
            field=models.ImageField(null=True, upload_to='ecommerce/static/ecommerce/images'),
        ),
    ]
