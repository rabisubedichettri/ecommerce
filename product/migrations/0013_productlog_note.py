# Generated by Django 5.0.7 on 2024-09-06 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_productcategory_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='productlog',
            name='note',
            field=models.CharField(default='ff', max_length=500),
            preserve_default=False,
        ),
    ]