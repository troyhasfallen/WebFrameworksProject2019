# Generated by Django 2.2 on 2019-04-21 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AetherMail', '0009_auto_20190420_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='read_status',
            field=models.CharField(choices=[('r', 'R'), ('u', 'U')], default='U', max_length=1),
        ),
    ]
