# Generated by Django 5.0.7 on 2024-08-23 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_product_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]