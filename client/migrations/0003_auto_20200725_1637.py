# Generated by Django 3.0.8 on 2020-07-25 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_auto_20200725_1625'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='active',
            new_name='clientactive',
        ),
        migrations.RemoveField(
            model_name='client',
            name='clientimg',
        ),
        migrations.RemoveField(
            model_name='client',
            name='link',
        ),
        migrations.AddField(
            model_name='client',
            name='clientlink',
            field=models.URLField(blank=True, null=True, verbose_name='Client Link'),
        ),
        migrations.AddField(
            model_name='client',
            name='clientlogo',
            field=models.ImageField(blank=True, null=True, upload_to='clients/', verbose_name='Client Logo'),
        ),
        migrations.AlterField(
            model_name='client',
            name='Desciption',
            field=models.TextField(null=True, verbose_name='Desciption'),
        ),
    ]
