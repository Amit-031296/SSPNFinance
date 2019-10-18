# Generated by Django 2.2.5 on 2019-10-18 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sspn_lead_manager_app', '0004_auto_20191018_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allleads',
            name='status',
            field=models.CharField(blank=True, choices=[('Pending', 'Pending'), ('InProcess', 'InProcess'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=920),
        ),
    ]