# Generated by Django 4.1.7 on 2023-12-18 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website1', '0014_alter_booking_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='id',
        ),
        migrations.AddField(
            model_name='booking',
            name='book_id',
            field=models.IntegerField(auto_created=True, default=0, primary_key=True, serialize=False, unique=True),
        ),
    ]
