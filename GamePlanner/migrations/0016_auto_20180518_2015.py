# Generated by Django 2.0.5 on 2018-05-18 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GamePlanner', '0015_auto_20180517_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='stage',
            field=models.CharField(choices=[('PLANNED', 'Planned'), ('IN_PROGRESS', 'In Progress'), ('TESTING', 'Testing'), ('COMPLETED', 'Completed')], default='PLANNED', max_length=200),
        ),
    ]
