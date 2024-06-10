from django.shortcuts import render

# Create your views here.
def teamintro(request):
    return render(request, "introduction/team.html")