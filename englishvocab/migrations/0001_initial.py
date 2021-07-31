# Generated by Django 3.2.5 on 2021-07-17 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('word', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('definition', models.CharField(max_length=300)),
                ('word_class', models.CharField(default='verb', max_length=30)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('last_seen', models.DateTimeField(auto_now=True)),
                ('seen_count', models.IntegerField()),
                ('correct_count', models.IntegerField()),
            ],
        ),
    ]
