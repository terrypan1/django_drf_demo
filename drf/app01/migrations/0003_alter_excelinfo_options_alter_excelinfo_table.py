# Generated by Django 4.2.8 on 2023-12-19 03:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_excelinfo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='excelinfo',
            options={'verbose_name': 'excel'},
        ),
        migrations.AlterModelTable(
            name='excelinfo',
            table='excelInfo',
        ),
    ]