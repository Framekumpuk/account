from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
import datetime
from django.utils import timezone

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def page(request):
    return render(request,"polls/page.html",'')

def question(request):
    error_message = 0
    try:
        question = request.POST['question']
        questionchoice = request.POST['questionchoice']
    except:
        error_message = 1
        question = ""
    else:
        questionchoice = questionchoice.split(",")
        if len(question) == 0 or len(questionchoice) < 1:
            error_message =  1
            question = ""
        else:
            q = Question(question_text = question, pub_date = timezone.now())
            q.save()
            for choicetxt in questionchoice:
                q.choice_set.create(choice_text = choicetxt, votes = 0)
    return render(request,"polls/question.html",{"question":question,"error_message":error_message})
