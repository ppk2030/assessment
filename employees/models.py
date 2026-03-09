from django.db import models
from django.core.validators import MinValueValidator


class Employee(models.Model):
    full_name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    salary = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(0)],
    )