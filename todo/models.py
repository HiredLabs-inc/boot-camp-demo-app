from django.db import models

# Create your models here.

class Task(models.Model):
    STATUSES = [
    	('Complete', 'Complete'),
        ('To Do', 'To Do'),
    ]
    title = models.CharField(max_length=100)
    due = models.DateField()
    status = models.CharField(max_length=30, choices=STATUSES, default='To Do')

    def __str__(self):
            return f'{self.title}, {self.status}'