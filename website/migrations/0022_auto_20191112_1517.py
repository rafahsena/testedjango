# Generated by Django 2.2.7 on 2019-11-12 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0021_auto_20191112_1509'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoria',
            options={'ordering': ['-qtd_acessos']},
        ),
    ]
