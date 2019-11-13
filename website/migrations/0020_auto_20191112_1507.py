# Generated by Django 2.2.7 on 2019-11-12 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0019_auto_20191107_1502'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='avaliacao',
            options={'verbose_name': 'Avaliação', 'verbose_name_plural': 'Avaliações'},
        ),
        migrations.AlterModelOptions(
            name='endereco',
            options={'ordering': ['cep'], 'verbose_name': 'Endereço', 'verbose_name_plural': 'Endereços'},
        ),
        migrations.AddField(
            model_name='categoria',
            name='qtd_acessos',
            field=models.PositiveIntegerField(default=0, verbose_name='Quantidade de acessos'),
            preserve_default=False,
        ),
    ]
