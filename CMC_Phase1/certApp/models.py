from django.db import models

# Create your models here.
class Certificate(models.Model):
    cname = models.CharField(max_length = 100)
    cissuer = models.CharField(max_length = 50)
    creceiver = models.CharField(max_length = 50)
    cgivendate = models.DateField()
    cexpirydate = models.DateField()
    crenewalteam = models.CharField(max_length = 50)
    cstatus = models.CharField(max_length = 20)
