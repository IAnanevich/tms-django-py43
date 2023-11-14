from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=20, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def full_name(self):
        return f'{self.last_name} {self.first_name}'


class Book(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1700), MaxValueValidator(2024)])
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    is_deleted = models.BooleanField(null=False, default=False)

    def __str__(self):
        return self.name

