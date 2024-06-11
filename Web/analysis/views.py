from django.shortcuts import render

# Create your views here.
def finedust(request):
    return render(request, "analysis_page/finedust.html")

def social_economy(request):
    return render(request, "analysis_page/social_economy.html")

def weather(request):
    return render(request, "analysis_page/weather.html")

def aerosol(request):
    return render(request, "analysis_page/aerosol.html")