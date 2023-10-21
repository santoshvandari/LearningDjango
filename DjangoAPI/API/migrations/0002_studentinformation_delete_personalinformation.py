# Generated by Django 4.2.6 on 2023-10-21 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentInformation',
            fields=[
                ('studentId', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('grade', models.IntegerField()),
                ('date', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'StudentData',
            },
        ),
        migrations.DeleteModel(
            name='PersonalInformation',
        ),
    ]
