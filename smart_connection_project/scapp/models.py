from django.db import models

# Create your models here.


class Posts(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    company_name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    company_descr = models.TextField()
    company_field = models.CharField(max_length=30)