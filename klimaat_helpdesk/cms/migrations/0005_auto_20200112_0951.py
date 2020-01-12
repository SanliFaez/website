# Generated by Django 2.2.9 on 2020-01-12 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0004_answer_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='categories',
        ),
        migrations.AddField(
            model_name='answer',
            name='excerpt',
            field=models.CharField(max_length=255, null=True, verbose_name='Short description'),
        ),
    ]