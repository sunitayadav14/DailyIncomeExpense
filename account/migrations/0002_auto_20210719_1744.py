# Generated by Django 3.0.7 on 2021-07-19 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='address',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='age',
            field=models.IntegerField(null=True),
        ),
    ]