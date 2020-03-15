# Generated by Django 2.0.3 on 2020-03-14 18:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20200314_0104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addressbook',
            name='user',
        ),
        migrations.AddField(
            model_name='userregistration',
            name='area',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userregistration',
            name='city',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='AddressBook',
        ),
    ]
