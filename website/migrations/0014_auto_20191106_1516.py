# Generated by Django 2.2.7 on 2019-11-06 15:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_avaliacao_comentario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacao',
            name='rating',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)], verbose_name='Rating'),
        ),
    ]