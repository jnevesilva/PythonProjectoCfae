# Generated by Django 4.2.4 on 2023-09-21 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_docente_agrupamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sessoes',
            name='faltas',
            field=models.ManyToManyField(blank=True, default='', to='app.docente'),
        ),
    ]