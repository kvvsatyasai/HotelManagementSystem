# Generated by Django 4.1.7 on 2023-11-10 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website1', '0005_customer_delete_register_delete_rooms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=50, unique=True),
        ),
    ]
