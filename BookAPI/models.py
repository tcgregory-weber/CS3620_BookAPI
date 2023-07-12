from django.db import models

# Create your models here.
class BookData(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    rating = models.IntegerField()
    image = models.ImageField(upload_to='images/', default='images/None/No-img.jpg')

    def __str__(self):
        return self.name