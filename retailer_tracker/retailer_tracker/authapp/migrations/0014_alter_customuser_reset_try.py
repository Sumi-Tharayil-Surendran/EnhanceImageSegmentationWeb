# Generated by Django 4.2.3 on 2023-08-10 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0013_customuser_reset_try'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='reset_try',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
