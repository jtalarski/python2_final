# Generated by Django 4.2 on 2023-04-28 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0005_ratingchoice_alter_pizza_current_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='title',
            new_name='pizza_to_rate',
        ),
    ]