# Generated by Django 2.0.3 on 2020-03-15 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_auto_20200316_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saleshistory',
            name='invoice_no',
            field=models.CharField(max_length=60),
        ),
    ]
