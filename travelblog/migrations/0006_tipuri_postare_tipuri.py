# Generated by Django 4.1.4 on 2023-01-04 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelblog', '0005_alter_postare_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipuri',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=5000)),
            ],
        ),
        migrations.AddField(
            model_name='postare',
            name='tipuri',
            field=models.CharField(default='calatorii', max_length=250),
        ),
    ]
