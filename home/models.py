from django.db import models

# Create your models here.
class location(models.Model):
    name = models.CharField(max_length= 40)

    def __str__(self):
        return self.name

class category(models.Model):
    cat = models.CharField(max_length= 30)

    def __str__(self):
        return self.cat

class Post(models.Model):
    image_url = models.ImageField(upload_to = 'posts/')
    title = models.CharField(max_length= 60)
    caption =models.TextField()
    location = models.ManyToManyField(location)
    category = models.ManyToManyField(category)

