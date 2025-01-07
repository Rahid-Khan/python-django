from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question,answer
from django.template import loader
from django.db.models import F
from django.urls import reverse
from django.views import generic

# Create your views here.


class IndexView(generic.ListView):
    template_name = "port/index.html"
    context_object_name = "latest_question_list"
    
    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("pub_date")[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = "port/detail.html"
    

class ResultsView(generic.DetailView):
    model = Question
    template_name = "port/results.html"

def vote(request , question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.answer_set.get(pk=request.POST["choice"])
    except (KeyError, answer.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "port/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.vote = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("port:results", args=(question.id,)))



