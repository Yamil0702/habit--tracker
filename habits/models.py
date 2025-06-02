from django.db import models

class Habit(models.Model): # Create your models here.
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
