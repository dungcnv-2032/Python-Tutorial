# Generated by Django 3.0.5 on 2020-04-22 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0015_auto_20200422_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(upload_to='images/', verbose_name='image'),
        ),
    ]
