# Generated by Django 3.1.2 on 2020-11-02 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_bug_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='bug_pics'),
        ),
    ]
