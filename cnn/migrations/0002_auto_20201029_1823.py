# Generated by Django 2.2.2 on 2020-10-29 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cnn', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classification',
            name='img',
            field=models.ImageField(upload_to=''),
        ),
    ]
