# Generated by Django 4.1.5 on 2023-09-01 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buisnessApp1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='productsTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=255)),
                ('productDesc', models.CharField(max_length=255)),
            ],
        ),
    ]
