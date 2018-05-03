from django.views.generic.list import ListView

from .models import Quiz


class QuestionBankView(ListView):
    model = Quiz
    template_name = 'quiz/qb.html'
    quiz = None
    paginate_by = 10

    def get_queryset(self):
        return Quiz.objects.all().order_by('pk')
