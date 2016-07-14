from django.db import models


class Content(models.Model):
    # MONTHS = (
    #     ('JAN', 'JANUARY'),
    #     ('FEB', 'FEBRUARY'),
    #     ('MAR', 'MARCH'),
    #     ('APR', 'APRIL'),
    #     ('MAY', 'MAY'),
    #     ('JUN', 'JUNE'),
    #     ('JUL', 'JULY'),
    #     ('AUG', 'AUGUST'),
    #     ('SEP', 'SEPTAMBER'),
    #     ('OCT', 'OCTOBER'),
    #     ('NOV', 'NOVEMBER'),
    #     ('DEC', 'DECEMBER')
    # )
    subject = models.CharField(max_length=50)
    content = models.TextField()
    publish_date = models.DateField()

    def __str__(self):
        return self.subject
