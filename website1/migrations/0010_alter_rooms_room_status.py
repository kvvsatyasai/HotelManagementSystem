# Generated by Django 4.1.7 on 2023-11-13 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website1', '0009_alter_rooms_room_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rooms',
            name='Room_Status',
            field=models.CharField(choices=[('Available', 'Available'), ('Not Available', 'Not Available')], max_length=60),
        ),
    ]
