from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pic')
    desc=models.TextField()
class team_mem(models.Model):
    name1= models.CharField(max_length=250)
    img1= models.ImageField(upload_to='pic1')
    desc1= models.TextField()


def __str__(self):
    return self.name
