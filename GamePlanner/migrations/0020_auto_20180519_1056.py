# Generated by Django 2.0.5 on 2018-05-19 10:56

from django.db import migrations
import simplemde.fields


class Migration(migrations.Migration):

    dependencies = [
        ('GamePlanner', '0019_designelement_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designelement',
            name='description',
            field=simplemde.fields.SimpleMDEField(blank=True, null=True, verbose_name='Element descriptioj'),
        ),
        migrations.AlterField(
            model_name='milestone',
            name='description',
            field=simplemde.fields.SimpleMDEField(verbose_name='Project Description'),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=simplemde.fields.SimpleMDEField(verbose_name='Project Description'),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=simplemde.fields.SimpleMDEField(verbose_name='Task Description'),
        ),
    ]
