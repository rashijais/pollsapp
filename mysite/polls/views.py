from django.shortcuts import render
from django.shortcuts import get_object_or_404, render

# Create your views here.

from django.http import HttpResponse
from .models import Question


def index(request):
    return HttpResponse("Hello World!!!")

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    return HttpResponse("You Are Looking At The Results Of Question %s" %question_id)

def vote(request, question_id):
    return HttpResponse("You Are Voting At Question %s" %question_id)

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)



