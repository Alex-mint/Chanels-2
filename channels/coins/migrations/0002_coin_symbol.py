# Generated by Django 4.0.6 on 2022-07-21 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coin',
            name='symbol',
            field=models.CharField(default='', max_length=250),
        ),
    ]