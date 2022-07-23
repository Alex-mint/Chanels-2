from django.db import models

class Coin(models.Model):
    name = models.CharField(max_length=250)
    symbol = models.CharField(max_length=250)
    price = models.FloatField(default=0, blank=True)
    rank = models.IntegerField(default=0, blank=True)
    url = models.URLField(default=0, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['rank']
    
