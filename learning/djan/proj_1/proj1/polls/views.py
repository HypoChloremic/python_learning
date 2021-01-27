# Shortcuts
from django.shortcuts import get_object_or_404, render

# http stuff...
from django.http import HttpResponse
from django.http import Http404


# Import the model class object, such that we can 
# interact with it here
from .models import Question

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
    
#     index_template = loader.get_template("polls/index.html")
#     index_context = {
#         "latest_question_list": latest_question_list,
#     } 

#     return HttpResponse(index_template.render(index_context, request))

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = { "latest_question_list": latest_question_list }
    return render(request, "polls/index.html", context)


# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#         context = {"question": question}
#         print("yoyo")
#     except Question.DoesNotExist:
#         # This is where the 404 error occurs, it will exist the 
#         # method
#         raise Http404("Question does not existttt")
#     return render(request, "polls/detail.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {"question": question}
    return render(request, "polls/detail.html", context)


def results(request, question_id):
    response = f"You're looking at the results of question {question_id}."
    return HttpResponse(response)


def vote(request, question_id):
    return HttpResponse(f"You're  voting on question {question_id}.")
