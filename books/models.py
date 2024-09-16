from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    number_of_pages = models.IntegerField()
    language = models.CharField(max_length=30)
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.title    