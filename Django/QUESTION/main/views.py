from django.shortcuts import render
from .models import Question, Major

def home(request):
    context = {

    }
    return render(request, 'home.html', context)

def question(request):
    major = request.POST.get('major')
    major2 = Major.objects.get(major=major)
    question = Question.objects.get(major=major2)