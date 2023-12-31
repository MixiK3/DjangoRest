# Generated by Django 4.2.2 on 2023-07-02 13:33

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0014_reports_name_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='FollowersCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.CharField(max_length=250)),
                ('user', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Подписчик',
                'verbose_name_plural': 'Подписчики',
            },
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название категории'),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='coding', max_length=255, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='post',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='post',
            name='snippet',
            field=models.CharField(max_length=255, verbose_name='Сниппет'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title_tag',
            field=models.CharField(max_length=255, verbose_name='Тег названия'),
        ),
    ]
