# Generated by Django 4.2.3 on 2023-08-06 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0005_customuser_date_of_birth_customuser_middle_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_of_birth',
            field=models.DateTimeField(null=True),
        ),
    ]
