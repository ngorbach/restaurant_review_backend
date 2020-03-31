# Generated by Django 3.0.4 on 2020-03-31 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('category', models.CharField(max_length=500)),
                ('country', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('zip', models.IntegerField()),
                ('website', models.URLField(max_length=250)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('opening_days', models.IntegerField(choices=[(1, 'Sunday'), (2, 'Monday'), (3, 'Tuesday'), (4, 'Wednesday'), (5, 'Thursday'), (6, 'Friday'), (7, 'Saturday')])),
                ('opening_time', models.TimeField()),
                ('closing_time', models.TimeField()),
                ('price_level', models.CharField(choices=[('LOW', '$'), ('MEDIUM', '$$'), ('HIGH', '$$$')], max_length=6)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
