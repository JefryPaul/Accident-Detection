# Generated by Django 5.1.4 on 2024-12-18 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0003_tbl_place'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_sample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_name', models.CharField(max_length=30)),
                ('admin_email', models.CharField(max_length=30)),
                ('admin_password', models.CharField(max_length=30)),
            ],
        ),
    ]
