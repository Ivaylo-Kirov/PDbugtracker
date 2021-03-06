# Generated by Django 3.1.2 on 2020-11-06 01:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_auto_20201104_1039'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(max_length=1000)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('bug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.bug')),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
    ]
