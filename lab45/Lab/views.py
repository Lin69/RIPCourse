from django.views.generic import ListView, DetailView
from django.views.generic.base import View, TemplateView

from Lab.models import Question


class IndexView(TemplateView):
    template_name = 'index.html'


class QuestionsView(ListView):
    model = Question

    template_name = 'question_list.html'


class QuestionView(DetailView):
    model = Question

    template_name = 'question.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Question.objects.all()\
            .filter(pk=self.kwargs['pk']).select_related()
        return context
