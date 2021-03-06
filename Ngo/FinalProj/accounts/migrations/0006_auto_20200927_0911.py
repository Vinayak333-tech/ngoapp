# Generated by Django 3.1.1 on 2020-09-27 03:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20200927_0401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donationdetail',
            name='donator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.donator'),
        ),
        migrations.AlterField(
            model_name='donationdetail',
            name='ngo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.ngo'),
        ),
        migrations.AlterField(
            model_name='donationdetail',
            name='requirement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.requirement'),
        ),
    ]
