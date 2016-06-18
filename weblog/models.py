from django.db import models

class Content(models.Model):
  subject = models.CharField(max_length = 50)
  content = models.TextField()
  publish_date = models.DateField()
