# Generated by Django 4.0.3 on 2022-04-29 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_events'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='picture',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]
