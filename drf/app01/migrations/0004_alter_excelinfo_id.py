# Generated by Django 4.2.8 on 2023-12-19 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_alter_excelinfo_options_alter_excelinfo_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='excelinfo',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='id'),
        ),
    ]