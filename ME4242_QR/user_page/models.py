from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    credit = models.IntegerField()

    def top_up(self,amount):
        self.credit += amount

    def one_play(self):
        self.credit -= 1