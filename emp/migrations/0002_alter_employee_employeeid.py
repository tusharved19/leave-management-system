# Generated by Django 3.2.7 on 2021-10-01 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employeeid',
            field=models.CharField(max_length=5, null=True, verbose_name='Employee Id Number'),
        ),
    ]
