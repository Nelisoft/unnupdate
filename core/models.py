from django.db import models
from django.contrib.auth.models  import User
from django_ckeditor_5.fields import CKEditor5Field
import datetime
from autoslug import AutoSlugField
from django.utils.text import slugify
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from ='name',unique=True,default=None,null=True)
    
    def save (self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            self.slug = f'{base_slug}'
            super().save(*args, **kwargs)
            
    def __str__(self):
        return self.name
    
    

# Create your models here.
class Post(models.Model):
    STATUS =(
        ('0','DRAFT'),
        ('1','PUBLISH')
    )
    SECTION = (
        ('Unapproved','Unapproved'),
        ('Recent','Recent'),
        ('Trending','Trending'),
        ('Featured','Featured'),
        ('Latest','Latest'),
        ('Most_viewed','Most_Viewed'),
        ('Popular','Popular'),
        ('top','top'),
        ('new','new')
    )
    img = models.ImageField(upload_to='Posts_img')
    title = models.CharField(max_length=255)
    body= CKEditor5Field(config_name='extends')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    Category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    blog_slug= AutoSlugField(populate_from='title',unique=True, default=None)
    status = models.CharField(choices=STATUS,max_length=1, default=0)
    section = models.CharField(choices=SECTION,max_length=100, default='Unapproved')
    main_post = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.title} - {self.author}'
    
    
class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post,related_name='commets',on_delete=models.CASCADE)
    blog_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
  
    comment = models.TextField()
    date = models.DateField(default=timezone.now)
    parent = models.ForeignKey('self',null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    
    def save(self,*args, **kwargs):
        if self.post:
            self.blog_id = self.post_id
            super().save(*args, **kwargs)
            
    
    def __str__(self):
        return self.name
                
    
    
class Contactinfo(models.Model):
    address = models.CharField(max_length=255)
    phone_number =models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    content = models.TextField()
    gmap =models.URLField()
    
    def __str__(self):
        return f'Contact information'