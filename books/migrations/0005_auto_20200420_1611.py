# Generated by Django 3.0.5 on 2020-04-20 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20200420_1608'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='book_history',
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name='book_history',
            constraint=models.UniqueConstraint(fields=('user', 'book'), name='user_book_unique'),
        ),
    ]
