# Generated by Django 4.2.7 on 2023-11-30 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0004_author_birth_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='is_free',
            field=models.BooleanField(default=True),
        ),
    ]
