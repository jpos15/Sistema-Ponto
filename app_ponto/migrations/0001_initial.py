# Generated by Django 2.2.1 on 2019-05-21 19:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CargoFuncionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao_cargo', models.CharField(max_length=128, verbose_name='Descriçaõ do cargo')),
            ],
        ),
        migrations.CreateModel(
            name='ConfiguracaoHora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao_conf_hora', models.CharField(max_length=128, verbose_name='Descrição da configuração da hora')),
                ('conf_hora_entrada_1', models.TimeField(blank=True, null=True, verbose_name='Hora de entrada 1')),
                ('conf_hora_saida_1', models.TimeField(blank=True, null=True, verbose_name='Hora de saída 1')),
                ('conf_hora_entrada_2', models.TimeField(blank=True, null=True, verbose_name='Hora de entrada 2')),
                ('conf_hora_saida_2', models.TimeField(blank=True, null=True, verbose_name='Hora de saída 2')),
            ],
        ),
        migrations.CreateModel(
            name='StatusPonto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=128, verbose_name='Descrição')),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128, verbose_name='Nome do funcionário')),
                ('cargo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_ponto.CargoFuncionario', verbose_name='Cargo do funcionário')),
                ('conf_hora', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_ponto.ConfiguracaoHora', verbose_name='COnfiguração da hora')),
                ('lider', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_ponto.Funcionario', verbose_name='Lider')),
                ('usuario', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
        ),
        migrations.CreateModel(
            name='Frequencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora_entrada_1', models.TimeField(blank=True, null=True, verbose_name='Hora de entrada 1')),
                ('hora_saida_1', models.TimeField(blank=True, null=True, verbose_name='Hora de saída 1')),
                ('hora_entrada_2', models.TimeField(blank=True, null=True, verbose_name='Hora de entrada 2')),
                ('hora_saida_2', models.TimeField(blank=True, null=True, verbose_name='Hora de saída 2')),
                ('data_resgistro', models.DateField(auto_now_add=True, null=True, verbose_name='Data do registro')),
                ('ip_registro', models.CharField(blank=True, default='10.1.1.14', editable=False, max_length=20, null=True)),
                ('juntificativa', models.TextField(blank=True, null=True)),
                ('funcionario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_ponto.Funcionario', verbose_name='Funcionário')),
                ('status_ponto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_ponto.StatusPonto', verbose_name='Tipo de ponto')),
            ],
        ),
    ]
