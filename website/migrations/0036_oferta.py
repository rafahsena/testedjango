# Generated by Django 2.2.7 on 2019-11-25 15:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0035_auto_20191122_1229'),
    ]

    operations = [
        migrations.CreateModel(
            name='Oferta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('banner', models.ImageField(blank=True, null=True, upload_to='website/images/banners', verbose_name='Banner')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor')),
                ('validade', models.DateTimeField(auto_now=True, verbose_name='Validade')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ofertas', to=settings.AUTH_USER_MODEL)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ofertas', to='website.Produto')),
            ],
            options={
                'ordering': ['-validade'],
            },
        ),
    ]
