from django.db import models


class Task(models.Model):
    
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=100)
    description = models.TextField()
    
    """
    name: String
    status: string choicefield ['draft', 'in progress', 'completed']
    description: string
    """
    pass

