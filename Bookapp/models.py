from django.db import models
import datetime

# Create your models here.
class Books(models.Model):
    bname = models.CharField(max_length=50)
    b_title = models.CharField(max_length=160)
    b_author = models.CharField(max_length=50)
    publish_date = models.DateField(default=datetime.date.today())
    total_quantity = models.BigIntegerField(max_length=5)
    aval_quantity = models.BigIntegerField(max_length=5, null=True, blank=True)

    def __str__(self):
        return self.bname