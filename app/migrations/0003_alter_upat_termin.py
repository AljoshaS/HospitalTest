# Generated by Django 4.0.4 on 2022-05-11 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_hospitalizacija_oddel_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upat',
            name='termin',
            field=models.DateTimeField(null=True),
        ),
    ]
