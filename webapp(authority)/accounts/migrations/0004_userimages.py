# Generated by Django 2.2 on 2020-07-23 17:53

import accounts.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200723_1941'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=accounts.models.get_image_filename, verbose_name='Image')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.UserDetails')),
            ],
        ),
    ]
