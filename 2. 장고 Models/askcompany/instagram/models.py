from django.db import models

class Post(models.Model) : #원하는 설계에 맞춰 작성하면 된다.
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)