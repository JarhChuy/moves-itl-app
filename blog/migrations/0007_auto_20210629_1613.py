# Generated by Django 2.2 on 2021-06-29 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_genero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='genero',
            field=models.IntegerField(choices=[(1, 'Accion'), (2, 'Terror'), (3, 'Infantil'), (4, 'Romanticas')], default=1),
        ),
    ]
