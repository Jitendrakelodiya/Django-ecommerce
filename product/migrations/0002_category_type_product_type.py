# Generated by Django 4.2 on 2023-06-06 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('image', models.ImageField(blank=True, upload_to='static/images')),
                ('price', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=20)),
                ('slug', models.SlugField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('Catg_Name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='product.category_type')),
            ],
        ),
        migrations.CreateModel(
            name='Product_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('image', models.ImageField(blank=True, upload_to='static/images')),
                ('price', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=20)),
                ('slug', models.SlugField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('Catg_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category_type')),
            ],
        ),
    ]