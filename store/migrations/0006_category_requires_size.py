# Generated by Django 4.2.16 on 2024-11-13 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_brand_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='requires_size',
            field=models.BooleanField(default=False),
        ),
    ]
