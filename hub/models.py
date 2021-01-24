from django.db import models
from django.db.models.fields import CharField


class StudentWebPage(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    file = models.FileField(upload_to='templates/hub/includes/uploads')
    
# Create your models here.
