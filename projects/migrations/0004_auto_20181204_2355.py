# Generated by Django 2.1.1 on 2018-12-05 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20181204_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='semester',
            field=models.CharField(max_length=20),
        ),
    ]
