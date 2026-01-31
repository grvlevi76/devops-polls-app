from django.shortcuts import render, get_object_or_404, redirect

# Create your views here - changed by goofy
from django.http import HttpResponse ,Http404, HttpResponseRedirect
from django.db.models import F
from django.urls import reverse
from django.views import generic
from .models import Question, Choice


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/details.html'


def vote(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    try: 
        selected_choice = question.choice_set.get(pk = request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        error_message = "u voted without selecting a choice , pls choose the option"
        context = {'error_message':error_message,'question':question}

        return render(request,'polls/details.html',context)
    else:
        selected_choice.votes = F("votes") +1
        selected_choice.save()

        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
    
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/result.html'
