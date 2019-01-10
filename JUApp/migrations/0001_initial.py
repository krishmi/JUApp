# Generated by Django 2.0.10 on 2019-01-10 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('dept', models.CharField(choices=[('Information Technology', 'Information Technology'), ('Construction', 'Construction'), ('Power', 'Power'), ('Printing', 'Printing'), ('Instrumentation', 'Instrumentation')], max_length=50)),
                ('sem', models.CharField(choices=[('First', 'First'), ('Second', 'Second'), ('Third', 'Third'), ('Fourth', 'Fourth'), ('Fifth', 'Fifth'), ('Sixth', 'Sixth'), ('Seventh', 'Seventh'), ('Eighth', 'Eighth')], default='First', max_length=10)),
            ],
        ),
    ]