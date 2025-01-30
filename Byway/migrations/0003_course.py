# Generated by Django 5.1.5 on 2025-01-25 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Byway', '0002_alter_category_options_category_image_category_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(max_length=50)),
                ('duration', models.CharField(max_length=50)),
                ('lectures', models.CharField(max_length=50)),
                ('autherImg', models.ImageField(blank=True, null=True, upload_to='home')),
                ('auther', models.CharField(max_length=50)),
                ('language', models.CharField(max_length=50)),
                ('thumbnailImg', models.ImageField(blank=True, null=True, upload_to='home/')),
                ('Ogprice', models.CharField(max_length=20)),
                ('Offprice', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
            },
        ),
    ]
