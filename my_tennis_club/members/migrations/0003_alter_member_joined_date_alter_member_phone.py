# Generated by Django 4.2.7 on 2023-12-05 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_member_joined_date_member_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='joined_date',
            field=models.DateField(default='2023-1-2'),
        ),
        migrations.AlterField(
            model_name='member',
            name='phone',
            field=models.IntegerField(default='0553898566'),
        ),
    ]