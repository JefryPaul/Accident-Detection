# Generated by Django 5.1.4 on 2024-12-19 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0005_rename_tbl_sample_tbl_admin'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tbl_place',
        ),
    ]
