# Generated by Django 3.1.4 on 2021-05-26 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_auto_20210526_1211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_image2',
        ),
        migrations.AddField(
            model_name='product',
            name='product_image0',
            field=models.ImageField(default='', upload_to='productimg'),
        ),
    ]
