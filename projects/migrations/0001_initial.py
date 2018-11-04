# Generated by Django 2.1.1 on 2018-11-03 05:20

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '__first__'),
        ('partners', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='EngagementType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=255, unique=True)),
                ('facilitator', models.CharField(blank=True, max_length=255)),
                ('description', models.TextField()),
                ('total_uno_students', models.IntegerField()),
                ('total_uno_hours', models.IntegerField()),
                ('total_k12_students', models.IntegerField(null=True)),
                ('total_k12_hours', models.IntegerField()),
                ('total_uno_faculty', models.IntegerField(blank=True, null=True)),
                ('total_other_community_members', models.IntegerField(blank=True, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('other_details', models.CharField(blank=True, max_length=100, null=True)),
                ('outcomes', models.CharField(blank=True, max_length=100, null=True)),
                ('total_economic_impact', models.DecimalField(blank=True, decimal_places=4, max_digits=15, null=True)),
                ('address_line1', models.CharField(blank=True, max_length=1024, null=True)),
                ('address_line2', models.CharField(blank=True, max_length=1024, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=25, null=True)),
                ('state', models.CharField(blank=True, max_length=15, null=True)),
                ('zip', models.IntegerField(blank=True, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('activity_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.ActivityType')),
                ('engagement_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.EngagementType')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectCampusPartner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_hours', models.IntegerField(blank=True, null=True)),
                ('total_people', models.IntegerField(blank=True, null=True)),
                ('wages', models.IntegerField(blank=True, null=True)),
                ('campus_partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partners.CampusPartner')),
                ('project_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectCommunityPartner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_hours', models.IntegerField(blank=True, null=True)),
                ('total_people', models.IntegerField(blank=True, null=True)),
                ('wages', models.IntegerField(default=22)),
                ('community_partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partners.CommunityPartner')),
                ('project_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectMission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mission_type', models.CharField(choices=[('Primary', 'Primary'), ('Secondary', 'Secondary'), ('Other', 'Other')], max_length=20)),
                ('mission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.MissionArea')),
                ('project_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(max_length=20, unique=True)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='semester',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.Semester'),
        ),
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.Status'),
        ),
    ]
