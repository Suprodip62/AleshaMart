# Generated by Django 4.1 on 2022-08-29 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0005_productimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('Cash On Delivery', 'Cash On Delivery'), ('Khalti', 'Khalti'), ('Esewa', 'Esewa'), ('paypal', 'paypal')], default='Cash On Delivery', max_length=20),
        ),
    ]
