# Generated by Django 4.1.4 on 2023-01-05 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelblog', '0007_alter_postare_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='postare',
            name='imagine_blog',
            field=models.ImageField(blank=True, null=True, upload_to='imagini/'),
        ),
    ]
