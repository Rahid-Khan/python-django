from django.db import models
import datetime
from django.utils import timezone


# Create your models here.
class Question(models.Model):
    test  = models.CharField(max_length=200)
    data = models.DateTimeField("data published")
    
    def __str__(self):
        return self.test
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    
    
class answer(models.Model):
    Question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_test = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_test
    
