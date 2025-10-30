from django.db import models

# Create your models here.

class customers(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    email = models.CharField(max_length=150, null=False, blank=False)
    phone = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.name