from django.db import models

# Create your models here
class Login(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    images = models.ImageField(upload_to='images/', default='No-image.jpg')



    def __str__(self):
        return self.title
