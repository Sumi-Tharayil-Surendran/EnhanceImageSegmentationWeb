# Generated by Django 4.2.3 on 2023-08-25 11:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0012_delete_candidatecertification_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='CreatedDate')),
                ('ImagePath', models.CharField(max_length=400, null=True, verbose_name='ImagePath')),
                ('Segment', models.CharField(max_length=200, null=True, verbose_name='Segment')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
