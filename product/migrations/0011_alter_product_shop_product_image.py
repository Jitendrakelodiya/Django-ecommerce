# Generated by Django 4.2.2 on 2023-06-16 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_alter_product_shop_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_shop',
            name='product_image',
            field=models.FileField(null=True, upload_to='media/static/images'),
        ),
    ]
