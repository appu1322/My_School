# Generated by Django 3.0.6 on 2020-06-12 07:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tut11', '0003_auto_20200612_1042'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChemistryComment',
            fields=[
                ('sr', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.TextField()),
                ('datestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tut11.ChemistryComment')),
                ('tut', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tut11.Chemistry')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
