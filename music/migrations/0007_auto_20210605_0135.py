# Generated by Django 3.1.7 on 2021-06-04 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_auto_20210604_1501'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trendings',
            name='id',
        ),
        migrations.AddField(
            model_name='trendings',
            name='trendsong_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
    ]
