# Generated by Django 4.1.7 on 2023-11-16 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website1', '0013_booking_customer_name_alter_booking_room_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('Booked', 'Booked'), ('Not Booked', 'Not Booked')], max_length=50),
        ),
    ]
