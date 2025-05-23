# Generated by Django 4.2.5 on 2023-09-25 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0003_imageupload'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('file', models.FileField(default=None, max_length=50, null=True, upload_to='images')),
            ],
            options={
                'db_table': 'FileUpload',
                'get_latest_by': 'datetime',
            },
        ),
    ]
