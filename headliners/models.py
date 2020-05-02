from django.db import models

class Headliner(models.Model):
    keyword = models.CharField(max_length=30)
    creationDate = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.keyword