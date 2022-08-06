# Generated by Django 4.0.6 on 2022-08-06 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_gender_movie_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='player',
            field=models.ManyToManyField(to='api.player'),
        ),
    ]