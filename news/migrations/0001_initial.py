# Generated by Django 2.2.5 on 2020-01-18 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('title', models.CharField(max_length=50)),
                ('posted_date', models.CharField(default='1, 18, 2020', max_length=20)),
                ('text', models.TextField(max_length=50000)),
                ('text_preview', models.TextField(max_length=2000)),
                ('entry', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]
