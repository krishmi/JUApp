# Generated by Django 2.0.10 on 2019-01-14 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JUApp', '0002_upload'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('password', models.CharField(default='', max_length=20)),
                ('dept', models.CharField(choices=[('Information Technology', 'Information Technology'), ('Construction', 'Construction'), ('Power', 'Power'), ('Printing', 'Printing'), ('Instrumentation', 'Instrumentation')], max_length=50)),
                ('roll', models.CharField(max_length=20)),
            ],
        ),
    ]
