from django.db import models
from django.contrib.auth.models import User

CATEGORY_CHOICES = [
    ('Breakfast', 'Breakfast'),
    ('Lunch', 'Lunch'),
    ('Dinner', 'Dinner'),
    ('Snack', 'Snack'),
]

class Meal(models.Model):
    objects = models.Manager()  # This is not needed, it’s automatically provided by Django
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    calories = models.PositiveIntegerField()
    date = models.DateField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Snack')

    def __str__(self):
        return f"{self.name} - {self.calories} kcal"
