from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 150, verbose_name = "Title")
    content = models.TextField(verbose_name = "Content")
    published = models.DateTimeField(verbose_name = "Publish date")
    image = models.FileField(upload_to="images/")
    
    def __str__(self):
        return self.title
        
class Comment(models.Model):
    name = models.CharField(max_length = 35, verbose_name = "User")
    content = models.TextField(verbose_name = "Comment")
    published = models.DateTimeField(verbose_name = "Publish date")
    article = models.ForeignKey(Article)
    
    def __str__(self):
        return self.name