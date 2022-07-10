from logging import PlaceHolder
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Таблица качеств компании
class Point(models.Model):
    title = models.CharField('Заголовок', max_length=20)
    textfield = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пункт"
        verbose_name_plural = "Пункты (Услуги)"

# Таблица сообщений с вкладки [Контакты]
class userMessage(models.Model):
    username = models.CharField('ФИО', max_length=50)
    email = models.EmailField('Email')
    phone = models.CharField('Номер телефона', max_length=20)
    textfield = models.TextField('Описание', max_length=500)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения (Контакты)"

# Таблица сообщений с вкладки [О нас]
class aboutMessage(models.Model):
    subject = models.CharField('Тема', max_length=80)
    to_email = models.EmailField('Email')
    plain_message = models.TextField('Описание', max_length=500)
    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = "Письмо"
        verbose_name_plural = "Письма (О нас)"

# Таблица новостей
class News(models.Model):
    title = models.CharField('Название статьи', max_length=100, unique=True)
    text = models.TextField('Текст статьи')
    date = models.DateTimeField('Дата', default=timezone.now)
    avtor = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    views = models.IntegerField('Просмотры', default=1)

    def get_absolute_url(self):
        return reverse('news-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости (Статьи)'