# Generated by Django 4.2.1 on 2023-05-08 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0011_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='title',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
