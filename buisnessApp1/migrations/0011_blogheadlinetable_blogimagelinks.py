# Generated by Django 4.1.5 on 2023-09-03 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buisnessApp1', '0010_blogheadlinetable_blogauthor'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogheadlinetable',
            name='blogImageLinks',
            field=models.CharField(default='null', max_length=255),
        ),
    ]
