# Generated by Django 4.2.4 on 2023-09-06 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(help_text=' password', max_length=128, null=True),
        ),
    ]