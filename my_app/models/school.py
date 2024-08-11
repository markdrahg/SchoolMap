from django.db import models

class School(models.Model):
    name = models.CharField(max_length=100)
    acceptance_rate = models.DecimalField(max_digits=5, decimal_places=2)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __str__(self):
        return self.name
