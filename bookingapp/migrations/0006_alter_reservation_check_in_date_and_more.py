# Generated by Django 5.0.1 on 2024-01-23 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingapp', '0005_delete_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='check_in_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='check_out_date',
            field=models.DateField(),
        ),
    ]