# Generated by Django 4.1 on 2022-08-25 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0010_remove_demande_paniers'),
    ]

    operations = [
        migrations.AddField(
            model_name='demande',
            name='ok',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
