from django.db import models

class Jikbang(models.Model) :
    objects = models.Manager()
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length = 300)
    body = models.TextField()
    
    def __str__(self):
        return self.title
# Create your models here.
