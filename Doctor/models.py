from django.db import models
from django.utils import timezone
class Stories(models.Model):
    story_file = models.FileField(upload_to='stories/')
    created_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.story_file)

# Create your models here.
