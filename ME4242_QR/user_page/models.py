from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    credit = models.IntegerField()

    def __str__(self):
        return self.username

    def top_up(self,amount):
        self.credit += amount
        self.save()

    def one_play(self):
        self.credit -= 1
        self.save()
    
    def enough(self):
        if self.credit > 0:
            return True 
