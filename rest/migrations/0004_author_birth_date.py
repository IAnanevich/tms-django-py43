# Generated by Django 4.2.7 on 2023-11-14 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0003_book_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
