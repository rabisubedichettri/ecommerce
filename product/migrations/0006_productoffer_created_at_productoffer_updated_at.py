# Generated by Django 5.0.7 on 2024-07-31 01:31

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_featuredproduct_mostsoldproduct_trendingproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='productoffer',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productoffer',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
