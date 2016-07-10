from django.db import models


class Content(models.Model):
    subject = models.CharField(max_length=50)
    content = models.TextField()
    publish_date = models.DateField()

    def __str__(self):
        return self.subject
