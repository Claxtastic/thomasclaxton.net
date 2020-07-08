from django.shortcuts import render

# Create your views here.

def home(request):
    # just render the static home page
    return render(request, "home.html")
