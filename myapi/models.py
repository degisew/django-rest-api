from django.db import models

# Create your models here.

class Hero(models.Model):
    name = models.TextField()
    alias = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)

    def __sttr__(self):
        return self.name