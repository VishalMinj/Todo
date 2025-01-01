from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Tasks(models.Model):
    PRIORITY=[
        ('max',"Maximum"),
        ('mid',"Medium"),
        ('min',"Minimum"),
    ]
    date=models.DateTimeField(default=timezone.now)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='task')
    priority=models.CharField(choices=PRIORITY,max_length=7)
    title=models.CharField(max_length=30)
    discription=models.TextField()

    def __str__(self):
        return f"{self.id}. {self.title}"
