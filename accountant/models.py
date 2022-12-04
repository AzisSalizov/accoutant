from django.db import models

# Create your models here.
class Profile(models.Model):
    login = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    
    def __str__(self):
        return self.login
    
class Category(models.Model):
    name = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name

class Note(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,verbose_name='profile')
    category = models.ForeignKey(Category,on_delete=models.CASCADE, verbose_name='category')
    
    def __str__(self):
        return self.name