# Generated by Django 3.1 on 2022-09-05 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20220904_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='variation_category',
            field=models.CharField(choices=[('size', 'size'), ('color', 'color')], max_length=100),
        ),
    ]