from django.db import models

class Amir(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()