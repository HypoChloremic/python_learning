import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    pub_date = models.DateTimeField("Date published")
    question_text = models.CharField(max_length=200)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    # TODO: what does ForeignKey do? we are passing it the 
    # Question class we just created
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    # The ForeignKey part
    # This allows us to connect the Choice 
    # part of the databse and link it to 
    # our Question, making Question a parent of sorts. 
    question = models.ForeignKey(
            Question, 
            on_delete = models.CASCADE,
            related_name="Choice_set")

    def __str__(self):
        return self.choice_text