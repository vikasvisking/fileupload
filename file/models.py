

# Create your models here.
from django.db import models

# Create your models here.
class File(models.Model):
    file = models.ImageField(upload_to='documents', blank=True)

    def __str__(self):
        return self.file.name

