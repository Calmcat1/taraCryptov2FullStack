# Generated by Django 4.1.5 on 2023-09-03 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buisnessApp1', '0009_blogheadlinetable_blogcontent1'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogheadlinetable',
            name='blogAuthor',
            field=models.CharField(default='null', max_length=255),
        ),
    ]