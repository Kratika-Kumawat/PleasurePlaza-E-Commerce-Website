# Generated by Django 3.0 on 2021-10-27 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20211027_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='info',
            field=models.CharField(default='NA', max_length=5000),
            preserve_default=False,
        ),
    ]
