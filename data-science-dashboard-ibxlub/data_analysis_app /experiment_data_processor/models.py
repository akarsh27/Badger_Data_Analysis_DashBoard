from django.db import models

class Experiment(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    observation_type = models.CharField(max_length=100)
    value = models.FloatField()

    def __str__(self):
        return f"{self.name} ({self.date}) - {self.observation_type}"
