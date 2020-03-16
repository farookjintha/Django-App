from django.db import models
import datetime
from django.utils import timezone

class Allcourses(models.Model):
    coursename = models.CharField(max_length=200)
    insname = models.CharField(max_length=100)
    startedfrom = models.DateTimeField("Started from")
    def __str__(self):
        return self.coursename
    
    def was_published_recently(self):
        return self.startedfrom >= timezone.now() - datetime.timedelta(days=1)

class details(models.Model):
    course = models.ForeignKey(Allcourses, on_delete = models.CASCADE)
    ct = models.CharField(max_length=500)
    your_choice = models.BooleanField(default = False)
    # sp = models.CharField(max_length=500)
    # il = models.CharField(max_length=500)
    def __str__(self):
        return str(self.ct)