from django.shortcuts import render, redirect
from predictions.models import Predictions
from django.http import HttpResponseRedirect
from django.urls import reverse

def main(request):
    loc = request.GET.get("loc", "108")

    predict = Predictions.objects.filter(loc = loc)

    for pred in predict:
        if isinstance(pred.time, int):
            pred.time = str(pred.time).zfill(2)
            pred.save()

    li = predict.values_list("date", flat=True).distinct()

    pred1 = []
    pred2 = []
    pred3 = []

    for pred in predict:
        if pred.date == li[0]:
            pred1.append(pred)
        elif pred.date == li[1]:
            pred2.append(pred)
        elif pred.date == li[2]:
            pred3.append(pred)


    context = {
        "pred1" : pred1,
        "pred2" : pred2,
        "pred3" : pred3,
    }

    return render(request, "main.html", context)