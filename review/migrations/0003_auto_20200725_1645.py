# Generated by Django 3.0.8 on 2020-07-25 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_auto_20200725_1637'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='revactive',
            new_name='active',
        ),
        migrations.AlterField(
            model_name='review',
            name='revimg',
            field=models.ImageField(blank=True, null=True, upload_to='revimg/', verbose_name='Client Image'),
        ),
    ]