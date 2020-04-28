from django.db import models

class Stock(models.Model):
    ticker = models.CharField(max_length=10)
    creationDate = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.ticker