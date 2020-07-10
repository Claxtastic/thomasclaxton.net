from django.shortcuts import render
from apps.about.models import Resume

# Create your views here.

def about(request):
    # get most recently uploaded resume
    # resume = Resume.objects.all().order_by('-id')[0]
    resume = Resume.objects.last()
    context = {
        'resume' : resume
    }

    return render(request, "about.html", context)
