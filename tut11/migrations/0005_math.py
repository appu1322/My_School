# Generated by Django 3.0.6 on 2020-06-19 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tut11', '0004_chemistrycomment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Math',
            fields=[
                ('sr', models.AutoField(primary_key=True, serialize=False)),
                ('slug', models.CharField(max_length=100)),
                ('title', models.CharField(default='', max_length=500)),
                ('desc', models.CharField(default='', max_length=5000)),
                ('videoFile', models.FileField(upload_to='tut11/math/', verbose_name='')),
            ],
        ),
    ]
