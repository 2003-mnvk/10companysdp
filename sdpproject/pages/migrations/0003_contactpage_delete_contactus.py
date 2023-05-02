# Generated by Django 4.1.7 on 2023-04-05 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_remove_customer_user_delete_product_delete_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('mail', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=10)),
                ('subject', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='ContactUs',
        ),
    ]
