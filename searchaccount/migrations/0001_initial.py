# Generated by Django 2.2.5 on 2019-10-20 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileKey',
            fields=[
                ('username', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=200)),
            ],
        ),
    ]
