# Generated by Django 5.0.7 on 2024-08-08 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0006_product_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_stream',
            field=models.BooleanField(default=False),
        ),
    ]
