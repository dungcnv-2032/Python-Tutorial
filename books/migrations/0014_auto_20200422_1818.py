# Generated by Django 3.0.5 on 2020-04-22 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0013_remove_book_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
