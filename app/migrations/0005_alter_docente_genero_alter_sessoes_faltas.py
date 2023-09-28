# Generated by Django 4.2.4 on 2023-09-25 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_sessoes_faltas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docente',
            name='genero',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=10, verbose_name='Género'),
        ),
        migrations.AlterField(
            model_name='sessoes',
            name='faltas',
            field=models.ManyToManyField(to='app.docente'),
        ),
    ]