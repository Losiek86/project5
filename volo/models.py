from django.db import models

# Create your models here.

class Volo(models.Model):
    STATUS_CHOICES = (
        ('received', 'Received'),
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('declined', 'Declined')
        )
    name = models.CharField(max_length = 35, verbose_name = "User")
    full_name = models.CharField(max_length=50, blank="False")
    phone_number = models.CharField(max_length=20, blank="False")
    town_or_city = models.CharField(max_length=40, blank="False")
    content = models.TextField(verbose_name = "About You")
    date = models.DateField()
    status = models.CharField(max_length=40, choices = STATUS_CHOICES)
    
    def __str__(self):
        return self.name