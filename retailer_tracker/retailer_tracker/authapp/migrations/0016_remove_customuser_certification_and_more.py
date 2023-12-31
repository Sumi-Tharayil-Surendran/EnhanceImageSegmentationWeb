# Generated by Django 4.2.3 on 2023-08-15 12:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_city_is_active'),
        ('authapp', '0015_candidateskill'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='certification',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='education',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='experience',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='language',
        ),
        migrations.CreateModel(
            name='CandidateLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='CreatedDate')),
                ('years_of_experience', models.CharField(max_length=200, null=True, verbose_name='YearsOfExperience')),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='candidate')),
                ('last_used', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_secondary_candidate_language', to='mainapp.standardcode', verbose_name='last_used')),
                ('proficiency', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_primary_candidate_language', to='mainapp.standardcode', verbose_name='proficiency')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CandidateExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='CreatedDate')),
                ('employer_name', models.CharField(max_length=200, null=True, verbose_name='EmployerName')),
                ('from_date', models.DateField(null=True, verbose_name='FromDate')),
                ('to_date', models.DateField(null=True, verbose_name='ToDate')),
                ('position', models.CharField(max_length=200, null=True, verbose_name='Position')),
                ('reason_for_leaving', models.CharField(max_length=500, null=True, verbose_name='ReasonForLeaving')),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='candidate')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CandidateEducation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='CreatedDate')),
                ('major', models.CharField(max_length=200, null=True, verbose_name='Major')),
                ('university', models.CharField(max_length=200, null=True, verbose_name='University')),
                ('year', models.IntegerField(null=True, verbose_name='Year')),
                ('gpa', models.IntegerField(null=True, verbose_name='GPA')),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='candidate')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.city')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.country')),
                ('degree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.standardcode')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CandidateCertification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='CreatedDate')),
                ('name', models.CharField(max_length=200, null=True, verbose_name='Name')),
                ('issued_by', models.CharField(max_length=200, null=True, verbose_name='IssuedBy')),
                ('year', models.IntegerField(null=True, verbose_name='Year')),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='candidate')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
