from django.shortcuts import render

# Create your views here.
def teamintro(request):
    return render(request, "introduction/team.html")

def projintro(request):
    return render(request, "introduction/project.html")