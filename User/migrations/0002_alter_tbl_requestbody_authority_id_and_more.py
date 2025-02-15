# Generated by Django 5.1.4 on 2025-01-13 05:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0015_rename_authority_status_tbl_hospital_hospital_status'),
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_requestbody',
            name='authority_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_authority'),
        ),
        migrations.AlterField(
            model_name='tbl_requestbody',
            name='hospital_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_hospital'),
        ),
        migrations.AlterField(
            model_name='tbl_requestbody',
            name='requestbody_status',
            field=models.IntegerField(default=0),
        ),
    ]
