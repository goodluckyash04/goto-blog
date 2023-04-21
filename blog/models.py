from django.db import models

# Create your models here.
class Blogger(models.Model):
    name = models.CharField( max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField( max_length=50)

    def __str__(self) :
        return self.email

class Blog(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField()
    pic = models.FileField(upload_to='blogimage', default='default.jpg')
    auther = models.ForeignKey(Blogger, on_delete=models.CASCADE)
    posted = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self) :
        return self.title