# Generated by Django 4.1.7 on 2024-01-10 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website1', '0031_alter_rooms_room_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rooms',
            name='Room_No',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
