# Generated by Django 4.2.3 on 2023-07-24 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posApp', '0004_salesitems'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='item_image'),
        ),
    ]
