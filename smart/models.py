from django.db import models

class Switches(models.Model):
    name = models.CharField(max_length=20)
    state = models.BooleanField(default=False)
    def __str__(self):
        return self.name