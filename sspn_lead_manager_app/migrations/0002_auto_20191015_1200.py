# Generated by Django 2.2.5 on 2019-10-15 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sspn_lead_manager_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allleads',
            name='product_interested_in',
            field=models.CharField(choices=[('Micro Finance', 'Micro Finance'), ('Instant Salary', 'Instant Salary'), ('Consumer Finance', 'Consumer Finance')], max_length=920),
        ),
        migrations.AlterField(
            model_name='allleads',
            name='status',
            field=models.CharField(choices=[('All Status', 'All Status'), ('Pending Status', 'Pending Status'), ('In Process Status', 'In Process Status'), ('Approved Status', 'Approved Status'), ('Rejected Status', 'Rejected Status')], max_length=920),
        ),
        migrations.AlterField(
            model_name='team',
            name='role',
            field=models.CharField(choices=[(2, 'admin'), (1, 'super_admin'), (3, 'team')], max_length=920),
        ),
    ]
