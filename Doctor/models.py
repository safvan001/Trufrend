from django.db import models
class Stories(models.Model):
    story_file = models.FileField(upload_to='stories/')
    def __str__(self):
        return str(self.story_file)

# Create your models here.
