from django.db import models
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
import cloudinary
from cloudinary_storage.storage import MediaCloudinaryStorage

# Create your models here.

class Home (models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255,blank=True,null=True)
    about=models.TextField()
    copyright= models.CharField(max_length=255,blank=True,null=True)
    address =  models.CharField(max_length=255,blank=True,null=True)
    phone=  models.CharField(max_length=255,blank=True,null=True)
    email= models.CharField(max_length=255,blank=True,null=True)
    contact_img=models.ImageField(upload_to='images' , blank=True,null=True)
    contact_headline=models.CharField(max_length=255,blank=True,null=True)
    def __str__(self) -> str:
        return self.title
    
class Contact (models.Model):
    sno = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255,blank=True,null=True)
    last_name = models.CharField(max_length=255,blank=True,null=True)
    email = models.CharField(max_length=255,blank=True,null=True)
    subject = models.CharField(max_length=255,blank=False,null=False)
    message = models.TextField(blank=True,null=True)
    


    def __str__(self) -> str:
        return (self.first_name+"  " + self.last_name)
    

class Category(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255,blank=True,null=True)

    def __str__(self) -> str:
        return self.title
    

class Post (models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255,blank=True,null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,blank=True,null=True)
    image= models.ImageField(upload_to='Blog_website_img', storage=MediaCloudinaryStorage() , blank=True,null=True)
    text = RichTextField()
    date = models.DateField(auto_now_add=True)
    slug = AutoSlugField(populate_from = 'title',null=True)

    def delete(self, *args, **kwargs):
 
        if self.image:
            try:

                public_id = self.image.url.split('upload/')[1].split('.')[0]
                print("Public ID:", public_id)

                cloudinary.uploader.destroy(public_id)
                print("Image deleted successfully.")
            except Exception as e:
                print("Error deleting image:", e)
        else:
            print("No image to delete.")
        
        super().delete(*args, **kwargs)

    def __str__(self) -> str:
        return self.title
    
    



class Comment (models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,blank=True,null=True)
    email=models.CharField(max_length=255,blank=True,null=True)
    post=models.ForeignKey(Post,on_delete=models.CASCADE ,null=True,blank=True)
    message=models.TextField()

    def __str__(self) -> str:
        return self.name