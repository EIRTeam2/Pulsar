# Generated by Django 2.0.5 on 2018-05-17 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GamePlanner', '0013_auto_20180517_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='final_cost',
            field=models.FloatField(default=0.0, verbose_name='Final cost'),
        ),
    ]