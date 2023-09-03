from django.db import models

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class BaseModel(models.Model):
    is_deleted = models.BooleanField(default=False)
    is_updated = models.DateTimeField(auto_now=True)
    is_created = models.DateTimeField(auto_now_add=True)
    id = models.IntegerField(primary_key=True,unique=True)

    class Meta:
        abstract = True

class Category(BaseModel):
    categoryName = models.CharField(max_length=100)

    def __str__(self):
        return self.categoryName
    
    
class SightseeingPlaces(BaseModel):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    image = models.ImageField(blank=True,null=True,upload_to="images/")
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100,null=True)
    country = models.CharField(max_length=100,blank=True)
    city = models.CharField(max_length=100,blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
