from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TODOO(models.Model):
    
    title=models.CharField(max_length=25)
    date=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} by {self.user.username}"