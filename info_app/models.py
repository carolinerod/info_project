from django.db import models

# Create your models here.
<<<<<<< HEAD
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pages = models.IntegerField()
    published_date = models.DateField()

    def __str__(self):
        return (f"""{{
                "title" : "{self.title}",
                "author" : "{self.author}",
                "pages" : {self.pages},
                "published_date" : "{self.published_date}"
                }}""")
=======
>>>>>>> 48b606f33ff92a87352ffb733161295fbe4f4df5
