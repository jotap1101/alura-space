# Generated by Django 5.0.4 on 2024-05-01 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotografia',
            name='descricao',
            field=models.TextField(blank=True, null=True),
        ),
    ]
