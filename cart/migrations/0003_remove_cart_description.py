# Generated by Django 4.1.2 on 2022-10-11 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_cart_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='description',
        ),
    ]
