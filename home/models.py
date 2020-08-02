from django.db import models

# Create your models here.
class tags(models.Model):
    name = models.CharField(max_length= 30)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length= 40)

    def __str__(self):
        return self.name


class Post(models.Model):
    image_url = models.ImageField(upload_to = 'posts/')
    title = models.CharField(max_length= 60)
    caption= models.TextField()
    tags= models.ManyToManyField(tags)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)

    @classmethod
    def get_posts(cls):
        posts = cls.objects.order_by('-title')
        return posts

    @classmethod
    def search_by_category(cls,search_term):
        post = cls.objects.filter(tags__icontains=search_term)
        return post