# Generated by Django 4.1.7 on 2023-11-10 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website1', '0006_alter_customer_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='email',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='password',
            new_name='Password',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='phone',
            new_name='Phone',
        ),
    ]
