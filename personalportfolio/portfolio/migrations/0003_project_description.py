# Generated by Django 5.0.4 on 2024-05-11 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.CharField(default=0, max_length=150),
            preserve_default=False,
        ),
    ]
