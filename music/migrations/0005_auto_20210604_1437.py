# Generated by Django 3.1.7 on 2021-06-04 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_auto_20210603_1423'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trendings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2000, null=True)),
                ('artist', models.CharField(max_length=2000, null=True)),
                ('tags', models.CharField(max_length=2000, null=True)),
                ('image', models.ImageField(null=True, upload_to='trends')),
                ('songs', models.FileField(null=True, upload_to='trends')),
            ],
        ),
        migrations.AlterField(
            model_name='song',
            name='songs',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='song',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
