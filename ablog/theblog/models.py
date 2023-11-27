from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from simple_history.models import HistoricalRecords



class Category(models.Model):
    name = models.CharField('Название категории', max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to='images/profile/')
    telegram_url = models.CharField(max_length=255, null=True, blank=True)


    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('home')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class Post(models.Model):
    title = models.CharField('Название', max_length=255)
    header_image = models.ImageField('Изображение', null=True, blank=True, upload_to='images/')
    title_tag = models.CharField('Тег названия', max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField('Описание', blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField('Категория', max_length=255, default='coding')
    snippet = models.CharField('Сниппет', max_length=255)
    likes = models.ManyToManyField(User, related_name='blog_posts')
    type_of_articles = models.CharField('Тип статьи', max_length=255)
    history = HistoricalRecords()

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Reports(models.Model):
    post = models.ForeignKey(Post, related_name="reports", on_delete=models.CASCADE)
    name_users = models.CharField(max_length=255, default='user')
    body = models.TextField()

    def __str__(self):
        return str(self.name_users)

    class Meta:
        verbose_name = 'Жалобы'
        verbose_name_plural = 'Жалобы'


class TypesOfArticles(models.Model):
    name = models.CharField('Название типа статьи', max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

    class Meta:
        verbose_name = 'Тип статьи'
        verbose_name_plural = 'Типы статей'


class FollowersCount(models.Model):
    follower = models.CharField(max_length=250)
    user = models.ForeignKey(Profile, related_name="subscribe", on_delete=models.CASCADE)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'

