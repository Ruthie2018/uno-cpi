# Generated by Django 2.1.1 on 2018-10-10 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0002_auto_20181007_1451'),
    ]

    operations = [
        migrations.RenameField(
            model_name='campuspartner',
            old_name='college',
            new_name='college_name',
        ),
        migrations.AlterField(
            model_name='campuspartner',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='university.Department'),
        ),
        migrations.AlterField(
            model_name='communitypartner',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='communitypartner',
            name='k12_level',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
