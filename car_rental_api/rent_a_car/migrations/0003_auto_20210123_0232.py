# Generated by Django 3.1.4 on 2021-01-22 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent_a_car', '0002_auto_20210122_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentcar',
            name='rent_from',
            field=models.DateTimeField(auto_now=True),
        ),
    ]