# Generated by Django 5.0.6 on 2024-06-05 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='celular',
            field=models.CharField(default='', max_length=11),
            preserve_default=False,
        ),
    ]