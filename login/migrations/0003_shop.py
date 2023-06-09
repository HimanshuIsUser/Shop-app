# Generated by Django 4.1.7 on 2023-03-11 04:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_delete_shop'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('longitude', models.CharField(blank=True, max_length=150, null=True)),
                ('latitude', models.CharField(blank=True, max_length=150, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
