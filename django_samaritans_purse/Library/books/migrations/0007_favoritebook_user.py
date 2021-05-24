# Generated by Django 4.0.dev20210521090054 on 2021-05-24 04:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('books', '0006_favoritebook'),
    ]

    operations = [
        migrations.AddField(
            model_name='favoritebook',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
