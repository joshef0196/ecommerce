# Generated by Django 2.0.3 on 2020-02-17 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_aboutus_emi_paymentmethod_privacypolicy_returnrefundpolicy_termsconditions_warranty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='brand_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Brands'),
        ),
        migrations.AlterField(
            model_name='products',
            name='sub_cat_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.SubSubCatagory'),
        ),
    ]
