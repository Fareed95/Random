# Generated by Django 5.0.7 on 2024-07-22 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0002_alter_botresponse_bot_response'),
    ]

    operations = [
        migrations.AddField(
            model_name='botresponse',
            name='question',
            field=models.CharField(default='default_value', max_length=255),
        ),
    ]
