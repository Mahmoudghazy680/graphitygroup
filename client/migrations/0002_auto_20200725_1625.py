# Generated by Django 3.0.8 on 2020-07-25 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ['clientname']},
        ),
        migrations.AddField(
            model_name='client',
            name='Desciption',
            field=models.TextField(null=True, verbose_name='Post Content'),
        ),
        migrations.AddField(
            model_name='client',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='client',
            name='clientimg',
            field=models.ImageField(blank=True, null=True, upload_to='pstimg/', verbose_name='Client Logo'),
        ),
        migrations.AddField(
            model_name='client',
            name='clientname',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Client Name'),
        ),
        migrations.AddField(
            model_name='client',
            name='link',
            field=models.URLField(blank=True, null=True, verbose_name=' Link'),
        ),
    ]
