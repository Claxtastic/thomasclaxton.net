from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.ImageField(upload_to='img')

    def __str__(self):
        return f"Project({self.title}, {self.description}, {self.technology}, {self.image})"
