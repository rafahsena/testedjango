# Generated by Django 2.2.6 on 2019-10-22 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('sobrenome', models.CharField(max_length=150, verbose_name='Sobrenome')),
                ('cpf', models.IntegerField(unique=True, verbose_name='CPF')),
                ('rg', models.IntegerField(blank=True, null=True, unique=True, verbose_name='RG')),
                ('data_nascimento', models.DateField(blank=True, null=True, verbose_name='Data de Nascimento')),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], default='M', max_length=1, verbose_name='Sexo')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('bairro', models.CharField(max_length=50, verbose_name='Bairro')),
                ('rua', models.CharField(max_length=50, verbose_name='Rua')),
                ('numero_casa', models.CharField(max_length=5, verbose_name='Número')),
                ('complemento', models.CharField(blank=True, max_length=50, null=True, verbose_name='Complemento')),
                ('cep', models.CharField(max_length=10, verbose_name='CEP')),
                ('cidade', models.CharField(max_length=120, verbose_name='Cidade')),
                ('uf', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RR', 'Roraima'), ('RO', 'Rondônia'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], default='AC', max_length=2, verbose_name='UF')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Loja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('nome_fantasia', models.CharField(max_length=150, verbose_name='Nome Fantasia')),
                ('cnpj', models.IntegerField(unique=True, verbose_name='CNPJ')),
                ('razao_social', models.CharField(max_length=150, unique=True, verbose_name='Razão Social')),
            ],
            options={
                'verbose_name': 'Loja',
                'verbose_name_plural': 'Lojas',
                'ordering': ['nome_fantasia'],
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('descricao', models.CharField(max_length=100, verbose_name='Descrição')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor')),
                ('qtd_estoque', models.IntegerField(verbose_name='Quantidade em estoque')),
                ('loja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produtos', to='website.Loja')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
                'ordering': ['descricao'],
            },
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('valor_total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, verbose_name='Valor')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Cliente', verbose_name='Cliente')),
                ('loja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendas', to='website.Loja')),
            ],
            options={
                'verbose_name': 'Venda',
                'verbose_name_plural': 'Vendas',
                'ordering': ['-update_at'],
            },
        ),
        migrations.CreateModel(
            name='VendaProduto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendas_produtos_produto', to='website.Produto')),
                ('venda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendas_produtos_venda', to='website.Venda')),
            ],
            options={
                'verbose_name': 'Venda de produto',
                'verbose_name_plural': 'Vendas de produtos',
                'ordering': ['-update_at'],
            },
        ),
        migrations.AddField(
            model_name='venda',
            name='produtos',
            field=models.ManyToManyField(related_name='vendas', through='website.VendaProduto', to='website.Produto'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='endereco',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clientes', to='website.Endereco'),
        ),
    ]