from django.db import models

# Create your models here.
class post(models.Model):
    title = models.TextField(max_length=200)
    content = models.TextField(max_length=7500)

    def __str__(self):
        return self.title