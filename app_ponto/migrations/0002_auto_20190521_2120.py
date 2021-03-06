# Generated by Django 2.1.7 on 2019-05-22 00:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_ponto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoPonto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=128, verbose_name='Descrição')),
            ],
        ),
        migrations.RenameField(
            model_name='frequencia',
            old_name='hora_entrada_1',
            new_name='hora_ponto',
        ),
        migrations.RemoveField(
            model_name='frequencia',
            name='hora_entrada_2',
        ),
        migrations.RemoveField(
            model_name='frequencia',
            name='hora_saida_1',
        ),
        migrations.RemoveField(
            model_name='frequencia',
            name='hora_saida_2',
        ),
        migrations.AlterField(
            model_name='frequencia',
            name='ip_registro',
            field=models.CharField(blank=True, default='192.168.43.5', editable=False, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='frequencia',
            name='tipo_ponto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_ponto.TipoPonto', verbose_name='Tipo ponto'),
        ),
    ]
