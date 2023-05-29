from django.db import models

class ToDo(models.Model):
    PRIORITY_CHOICES = (
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    )

    title = models.CharField(max_length=255)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)

    def __str__(self):
        return self.title
