# Generated by Django 5.2 on 2025-05-09 01:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardapio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='produto_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='cardapio.produtos'),
        ),
    ]
