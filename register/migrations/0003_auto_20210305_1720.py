# Generated by Django 3.1.3 on 2021-03-05 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_auto_20210302_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delegate',
            name='topicPref1',
            field=models.CharField(choices=[(0, 'CLIMATE ACTION'), (1, 'FINANCIAL INDEPENDENCE OF WOMEN'), (2, 'RURAL ILLITERACY AND UNEMPLOYMENT'), (3, 'YOUTH PRIVACY AND SOCIAL MEDIA'), (4, 'ZERO HUNGER')], default=None, max_length=2000),
        ),
    ]
