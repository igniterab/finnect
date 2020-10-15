# Generated by Django 3.0.6 on 2020-10-04 17:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('profession', models.TextField(blank=True, default='not given', max_length=100, null=True)),
                ('position', models.TextField(default='not given', max_length=100)),
                ('about', models.TextField(default='not given', max_length=100)),
                ('birthdate', models.DateTimeField(blank=True, null=True)),
                ('phone_number', models.CharField(default='not given', max_length=100)),
                ('address', models.TextField(default='not given', max_length=100)),
                ('facebook', models.TextField(default='not given', max_length=100)),
                ('linkedin', models.TextField(default='not given', max_length=100)),
                ('twitter', models.TextField(default='not given', max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]