# Generated by Django 3.1.4 on 2021-01-22 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rent_a_car', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rentcar',
            options={'verbose_name_plural': 'Rent Car'},
        ),
        migrations.AlterModelOptions(
            name='vehicles',
            options={'verbose_name_plural': 'Vehicle'},
        ),
        migrations.AlterModelTable(
            name='rentcar',
            table='Rent Car',
        ),
        migrations.AlterModelTable(
            name='vehicles',
            table='Vehicle',
        ),
    ]