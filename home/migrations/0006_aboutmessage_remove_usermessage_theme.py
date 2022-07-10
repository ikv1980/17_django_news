# Generated by Django 4.0.5 on 2022-07-10 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_usermessage_theme'),
    ]

    operations = [
        migrations.CreateModel(
            name='aboutMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(max_length=80, verbose_name='Тема')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('textfield', models.TextField(max_length=500, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Письмо',
                'verbose_name_plural': 'Письма (О нас)',
            },
        ),
        migrations.RemoveField(
            model_name='usermessage',
            name='theme',
        ),
    ]