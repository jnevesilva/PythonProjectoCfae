# Generated by Django 4.2.4 on 2023-09-21 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_sessoes_faltas_alter_sessoes_localformacao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docente',
            name='agrupamento',
            field=models.CharField(choices=[('AEAS', 'Agrupamento de Escolas Abel Salazar'), ('AEPOL', 'Agrupamento de Escolas Prof. Óscar Lopes'), ('ESAG', 'Escola Secundária Auguto Gomes'), ('ZARCO', 'Escola Secundária João Gonçalves Zarco'), ('ESAG', 'Escola SEcundária Augusto Gomes'), ('ESBN', 'Escola secundária da Boa Nova'), ('AEP', 'Agrupamento de Escolas de Perafita'), ('AESH', 'Agrupamento de Escolas da Senhora da Hora'), ('AEFPO', 'Agrupamento de Escolas Fernando Pinto de Oliveira'), ('AEJDS', 'Agrupamento de Escolas José Domigues dos Santos'), ('AEIP', 'Agrupamento de Escolas de Irmãos Passos'), ('AESH', 'Agrupamento de Escolas da Senhora da Hora')], default='ZARCO', max_length=5, verbose_name='nivel de ensino'),
        ),
    ]
