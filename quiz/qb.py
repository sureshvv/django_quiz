from django.views.generic.list import ListView

from .models import Question, Quiz
# from multichoice.models import MCQuestion


class QuestionBankView(ListView):
    model = Question
    template_name = 'quiz/qb.html'
    quiz = None
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        self.quiz = Quiz.objects.get(pk=int(kwargs['quiz']))
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['quiz'] = self.quiz
        return context

    def get_queryset(self):
        return self.quiz.get_questions()
