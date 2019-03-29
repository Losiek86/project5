from django.db import models

# Create your models here.

class Pupil(models.Model):
    name = models.CharField(max_length = 150, verbose_name = "Title")
    content = models.TextField(verbose_name = "Content")
    published = models.DateTimeField(verbose_name = "Publish date")
    image = models.FileField(upload_to="images/")
    age = models.DateField(verbose_name = "Date of Birth")
    breed = models.TextField(verbose_name="Breed")
    
    def __unicode__(self):
        return self.title