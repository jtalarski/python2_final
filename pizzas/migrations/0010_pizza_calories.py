# Generated by Django 4.2 on 2023-05-01 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0009_submission_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='calories',
            field=models.IntegerField(default=0),
        ),
    ]
