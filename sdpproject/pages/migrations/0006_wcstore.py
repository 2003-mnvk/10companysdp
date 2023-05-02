# Generated by Django 4.1.7 on 2023-04-30 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_sellpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wcstore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='photos')),
            ],
        ),
    ]
