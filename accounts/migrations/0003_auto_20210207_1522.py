# Generated by Django 3.0 on 2021-02-07 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20201104_2046'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default=0, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(default=0, max_length=80),
            preserve_default=False,
        ),
    ]
