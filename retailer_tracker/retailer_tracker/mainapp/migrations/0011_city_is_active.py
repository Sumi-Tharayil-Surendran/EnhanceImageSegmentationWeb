# Generated by Django 4.2.3 on 2023-08-15 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_rename_country_id_city_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='is_active',
            field=models.BooleanField(null=True, verbose_name='IsActive'),
        ),
    ]
