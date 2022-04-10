# Generated by Django 4.0.3 on 2022-04-09 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover_photo',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
