# Generated by Django 4.1.10 on 2023-09-03 18:09

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('selling_price', models.FloatField()),
                ('discription', models.TextField()),
                ('composition', models.TextField(default='')),
                ('prodapp', models.TextField(default='')),
                ('category', models.CharField(choices=[('M', 'Men'), ('W', 'Women'), ('K', 'Kids'), ('S', 'Sale')], max_length=2)),
                ('product_image1', models.ImageField(upload_to='product')),
                ('product_image2', models.ImageField(upload_to='product')),
                ('product_image3', models.ImageField(upload_to='product')),
                ('product_image4', models.ImageField(upload_to='product')),
            ],
        ),
    ]