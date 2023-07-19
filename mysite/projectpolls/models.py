from django.db import models

# Create your models here.
from django.utils import timezone

class Question(models.Model):
    question_text=models.CharField(max_length=250)
    pub_date=models.DateTimeField()

    def __str__(self):
        return f'Question obj:{self.question_text}'

class Choice(models.Model):
    choice_text=models.CharField(max_length=250)
    votes=models.IntegerField(default=0)
    question=models.ForeignKey(Question,on_delete=models.CASCADE)

    def __str__(self):
        return f'Choice obj:{self.choice_text}'
    
# q1=Question(question_text="what is the colour of sky",pub_date=timezone.now())
# q1.save()

# q2=Question(question_text="how many states are there in india?",pub_date=timezone.now())
# q2.save()

# q1_c1=Choice(choice_text='blue',question=q1)
# q1_c2=Choice(choice_text='red',question=q1)
# q1_c3=Choice(choice_text='black',question=q1)
# q1_c1.save()
# q1_c2.save()
# q1_c3.save()

# q2_c1=Choice(choice_text='27',question=q2)
# q2_c2=Choice(choice_text='28',question=q2)
# q2_c3=Choice(choice_text='29',question=q2)
# q2_c1.save()
# q2_c2.save()
# q2_c3.save()