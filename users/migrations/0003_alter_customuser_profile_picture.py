# Generated by Django 4.1.5 on 2023-01-15 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_picture',
            field=models.ImageField(default='profile-pic-MD.jpg', upload_to=''),
        ),
    ]
