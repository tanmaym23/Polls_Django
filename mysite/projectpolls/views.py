from django.shortcuts import render , reverse
from django.http import HttpResponse ,HttpResponseRedirect
from projectpolls.models import Question,Choice
# Create your views here.

# def index (requests):
    
#     return HttpResponse("hello! Polls app index.")

# def show_polls(requests):
#     q1=Question.objects.get(id=1)
#     q2=Question.objects.get(id=2)

#     context={
#         'q1': q1.question_text,
#         'q2': q2.question_text
#     }
#     return render(requests,'polls/index.html',context)

def index(requests):
    # This page will show the list of all questions.
    questions=Question.objects.all()
    context={
        'question_list':[question for question in questions]
    }
    return render(requests,'polls/index.html',context)

def details(request,question_id):
    #This page will show the question no. {question_id} with all its choices.
    question=Question.objects.get(id=question_id)
    context={
        'question':question
    }
    return render(request,'polls/detail.html',context)

def result(request,question_id):
    # This page will show the result of question no. {question_id}.
    question =Question.objects.get(id=question_id)
    context={
        'question':question
    }
    return render(request,'polls/result.html',context)

def vote(request,question_id):
    # you are voting for question no. {question_id}
    question=Question.objects.get(id=question_id)

    try:
        # primary key of selected option
        choice_pk = request.POST['my_selection']

        choice=Choice.objects.get(id=choice_pk)
    # redisplaying the question page
    except(KeyError,Choice.DoesNotExist):
        return render(request,'polls/detail.html',{question:question,"error message":"u didnt deect any choice"},)
    
    # if option is selected
    else:
        choice.votes +=1
        choice.save()
        return HttpResponseRedirect(reverse('result',args=(question.id,)))
    