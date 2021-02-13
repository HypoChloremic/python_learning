# Shortcuts
from django.shortcuts import get_object_or_404, render, reverse

# http stuff...
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404

# Import the model class object, such that we can 
# interact with it here
from .models import Question, Choice

# for the generic views
from django.views import generic

# The utils
from django.utils import timezone

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        response = Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by("-pub_date")[:5]
        return response

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

class ResultsView(generic.DetailView): 
    model = Question
    template_name = "polls/results.html"

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
    try:
        selected_choice = question.Choice_set.get(pk=request.POST["choice"])
    
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
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     print(latest_question_list)
#     context = { "latest_question_list": latest_question_list }
#     return render(request, "polls/index.html", context)

# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     context = {"question": question}
#     return render(request, "polls/detail.html", context)

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)

#     return render(request, "polls/results.html", {"question": question})
