from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
class Category(models.Model):
    image = models.FileField(upload_to='categories/', blank=True, null=True, validators=[FileExtensionValidator(allowed_extensions=['svg'])])  # Store images
    title = models.CharField(max_length=50)  # Short text for the title
    description = models.CharField(max_length=20)

    class Meta:  
        ordering = ['title']  
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):  
        return self.title


class Course(models.Model):
    Title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    rating = models.CharField(max_length=50)
    duration =models.CharField(max_length=50)
    lectures = models.CharField(max_length=50)
    autherImg = models.FileField(upload_to='home/', blank=True, null=True, validators=[FileExtensionValidator(allowed_extensions=['svg'])])
    auther=models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    thumbnailImg = models.FileField(upload_to='home/', blank=True, null=True, validators=[FileExtensionValidator(allowed_extensions=['svg','jpg','jpeg'])])
    Ogprice = models.CharField(max_length=20)
    Offprice = models.CharField(max_length=20)


    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.Title