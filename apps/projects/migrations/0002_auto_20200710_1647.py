# Generated by Django 2.2.13 on 2020-07-10 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='repo',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='img'),
        ),
    ]