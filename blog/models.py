from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class Image(models.Model):
    image = models.ImageField('Kartinka', upload_to='images/')
    title = models.CharField('Nazvanie' , max_length=255)

    class Meta:
        verbose_name = "Kartinki"
        verbose_name_plural = "Kartinki"

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Avtor")
    title = models.CharField('Zagalovok', max_length=255)
    video = models.FileField('Video', upload_to='videos/')
    preview = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True, verbose_name='Prevyushka')
    gallery = models.ManyToManyField(Image,  blank=True, verbose_name='Galereya', related_name='posts')
    content = models.TextField('Opisaniya')
    date = models.DateTimeField('Data', default=timezone.now)
    featured = models.BooleanField('Rekomedovini', default=False)
    publish= models.BooleanField('Publikatsiya', default=False)

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Video"
    
class Like(models.Model):
        post = models.ForeignKey(Post, on_delete=models.CASCADE)
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        date= models.DateTimeField(default=timezone.now)

class Dislike(models.Model):
        post = models.ForeignKey(Post, on_delete=models.CASCADE)
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        date= models.DateTimeField(default=timezone.now)

class View(models.Model):
     post = models.ForeignKey(Post, on_delete=models.CASCADE)
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     date = models.DateTimeField(default=timezone.now)

class Comment(models.Model):
     author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Avtor")
     post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="Video")
     text = models.TextField('Tekst komentariya')
     date = models.DateTimeField('date', default=timezone.now)
     publish = models.BooleanField('Publikatsiya', default=False)

class Category(models.Model):
          

 class Meta:
     verbose_name = "Komentariya"
     verbose_name_plural = "Komentariya"   

