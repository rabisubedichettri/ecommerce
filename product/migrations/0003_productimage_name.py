# Generated by Django 5.0.7 on 2024-07-26 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_productcategory_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='name',
            field=models.CharField(default='rabi', max_length=100),
            preserve_default=False,
        ),
    ]
