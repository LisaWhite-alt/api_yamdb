# Generated by Django 3.0.5 on 2021-06-09 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20210609_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='category',
            field=models.ForeignKey(blank=True, db_column='category', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='titles', to='api.Category', verbose_name='Категория'),
        ),
    ]
