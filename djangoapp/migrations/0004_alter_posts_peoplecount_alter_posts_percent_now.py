# Generated by Django 4.0.4 on 2022-04-20 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0003_posts_peoplecount_posts_percent_now'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='Peoplecount',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='posts',
            name='percent_now',
            field=models.CharField(blank=True, default=0, max_length=100, null=True),
        ),
    ]
