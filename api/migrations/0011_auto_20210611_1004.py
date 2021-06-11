# Generated by Django 3.0.5 on 2021-06-11 10:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('api', '0010_auto_20210610_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='genre',
            field=models.ManyToManyField(blank=True, db_index=True,
                                         related_name='titles', to='api.Genre',
                                         verbose_name='Жанр'),
        ),
    ]
