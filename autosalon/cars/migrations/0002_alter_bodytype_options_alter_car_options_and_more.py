# Generated by Django 5.2.1 on 2025-05-23 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bodytype',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='car',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='manufacturer',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='payment',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='position',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='staff',
            options={'managed': False},
        ),
    ]
