# Generated by Django 4.2.8 on 2023-12-17 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(max_length=10, verbose_name='用戶名')),
                ('done', models.BooleanField(max_length=10, verbose_name='是否完成')),
            ],
            options={
                'verbose_name': 'todo',
                'db_table': 'todoInfo',
            },
        ),
    ]