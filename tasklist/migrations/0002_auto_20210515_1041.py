# Generated by Django 2.2.12 on 2021-05-15 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasklist', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addtask',
            old_name='task_name',
            new_name='name',
        ),
    ]