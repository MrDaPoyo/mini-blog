from django.db import models

from django.conf import settings
User = settings.AUTH_USER_MODEL

# Create your models here.
class post(models.Model):
    author = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.TextField(max_length=200)
    content = models.TextField(max_length=7500)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title