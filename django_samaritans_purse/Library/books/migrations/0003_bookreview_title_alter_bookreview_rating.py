# Generated by Django 4.0.dev20210521090054 on 2021-05-23 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_bookreview_date_created_alter_bookreview_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookreview',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='bookreview',
            name='rating',
            field=models.IntegerField(blank=True, choices=[(1, 'Do Not Pick This Up 1 Star'), (2, 'Just Did Not Like It 2 Stars'), (3, 'Mixed Feelings 3 Stars'), (4, 'Enjoyed It 4 Stars'), (5, 'New Favorite 5 Stars')], null=True),
        ),
    ]
