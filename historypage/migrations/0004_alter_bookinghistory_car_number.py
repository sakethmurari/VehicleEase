# Generated by Django 5.1.2 on 2024-12-16 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historypage', '0003_bookinghistory_actual_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinghistory',
            name='car_number',
            field=models.CharField(default='null', max_length=100, unique=True),
        ),
    ]
