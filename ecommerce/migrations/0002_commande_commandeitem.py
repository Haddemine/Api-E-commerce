# Generated by Django 4.0.6 on 2022-08-14 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modePaiment', models.CharField(max_length=50)),
                ('statut', models.CharField(max_length=100)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='ecommerce.client')),
            ],
        ),
        migrations.CreateModel(
            name='commandeitem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.IntegerField()),
                ('commande', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commande', to='ecommerce.commande')),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='ecommerce.produit')),
            ],
        ),
    ]