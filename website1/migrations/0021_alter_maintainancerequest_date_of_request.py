# Generated by Django 4.1.7 on 2023-12-29 13:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website1', '0020_maintainancerequest_date_of_request'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintainancerequest',
            name='date_of_request',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
