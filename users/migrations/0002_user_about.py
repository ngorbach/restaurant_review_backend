# Generated by Django 3.0.4 on 2020-04-02 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='about',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
    ]
