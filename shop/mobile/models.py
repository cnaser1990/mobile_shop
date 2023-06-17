from django.db import models
from django.utils import timezone
# Create your models here.

class Mobile(models.Model):
    name=models.CharField(max_length=20 , default='iphone 8' )
    price=models.IntegerField()
    description=models.TextField()
    storage=models.CharField(max_length=30)
    created=models.DateTimeField(auto_now_add=True)
    edited=models.DateTimeField(auto_now=True)
    published=models.DateTimeField(default=timezone.now)
    photo=models.ImageField(upload_to='mobile')
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering=('name',)