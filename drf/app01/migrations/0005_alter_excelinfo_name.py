# Generated by Django 4.2.8 on 2023-12-19 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_alter_excelinfo_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='excelinfo',
            name='name',
            field=models.CharField(max_length=50, verbose_name='用戶名'),
        ),
    ]
