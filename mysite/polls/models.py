import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    """question database model for simple poll app"""
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        """display Question object instance attributes"""
        return  "question_text: " + self.question_text \
                + "\npub_date:" + self.pub_date.__str__()

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    """choice database model for simple poll app"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """display Choice object instance attributes"""
        return "choice_text: " + self.choice_text
