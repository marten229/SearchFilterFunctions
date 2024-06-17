# Generated by Django 5.0.6 on 2024-05-30 14:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='restaurant_photos/')),
                ('cuisine', models.CharField(choices=[('Italian', 'Italian'), ('Chinese', 'Chinese'), ('Mexican', 'Mexican'), ('Indian', 'Indian'), ('French', 'French'), ('Japanese', 'Japanese'), ('Thai', 'Thai'), ('Other', 'Other')], max_length=50)),
                ('rating', models.DecimalField(decimal_places=2, default=0.0, max_digits=3)),
                ('available', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
