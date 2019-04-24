# Generated by Django 2.2 on 2019-04-18 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_user', models.CharField(max_length=20)),
                ('to_user', models.CharField(max_length=20)),
                ('subject', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('timestamp', models.DateTimeField()),
                ('category', models.CharField(max_length=1)),
                ('read_status', models.CharField(max_length=1)),
            ],
        ),
    ]
