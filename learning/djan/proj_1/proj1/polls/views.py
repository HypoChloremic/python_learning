# Shortcuts
from django.shortcuts import get_object_or_404, render

# http stuff...
from django.http import HttpResponse
from django.http import Http404

# Import the model class object, such that we can 
# interact with it here
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    print(latest_question_list)
    context = { "latest_question_list": latest_question_list }
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {"question": question}
    return render(request, "polls/detail.html", context)

def results(request, question_id):
    response = f"You're looking at the results of question {question_id}."
    return HttpResponse(response)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.Choice_set.get(pk=request.POST("choice"))
    
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form
        return render(request, "polls/detail.html", {
            "question": question,
            "error_message": "You didn't select a choice.",
        })
    
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after
        # successfully dealing with POST data. 
        # This prevents data from being posted twice
        # if a user hits the Back button
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     index_template = loader.get_template("polls/index.html")
#     index_context = {
#         "latest_question_list": latest_question_list,
#     } 
#     return HttpResponse(index_template.render(index_context, request))

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
