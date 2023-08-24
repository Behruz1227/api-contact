from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=55)
    email = models.EmailField()
    number = models.CharField(max_length=13)
    subject = models.CharField(max_length=155)
    message = models.TextField()

    def __str__(self):
        return self.name
