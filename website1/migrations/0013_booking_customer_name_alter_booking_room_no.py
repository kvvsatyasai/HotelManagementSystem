# Generated by Django 4.1.7 on 2023-11-13 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website1', '0012_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='Customer_Name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='website1.customer'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='Room_No',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='website1.rooms'),
        ),
    ]
