# Generated by Django 4.0.6 on 2022-07-15 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipeBook', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
