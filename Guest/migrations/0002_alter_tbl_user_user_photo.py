# Generated by Django 5.1.4 on 2024-12-20 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_user',
            name='user_photo',
            field=models.FileField(upload_to='Assets/Files/User/Photo/'),
        ),
    ]
