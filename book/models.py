from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=255)
    isbn = models.CharField(max_length=15)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - ISBN: {self.isbn}"
