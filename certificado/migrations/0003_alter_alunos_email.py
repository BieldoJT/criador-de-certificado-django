# Generated by Django 5.1.3 on 2024-12-18 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificado', '0002_alter_alunos_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alunos',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
