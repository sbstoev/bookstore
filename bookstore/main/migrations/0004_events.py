# Generated by Django 4.0.3 on 2022-04-28 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField(blank=True, null=True)),
                ('city', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
