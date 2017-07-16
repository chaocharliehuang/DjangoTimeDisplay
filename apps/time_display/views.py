from django.shortcuts import render, redirect, HttpResponse
from time import localtime, strftime

# Create your views here.
def index(request):
    context = {
        "date": strftime("%b %d, %Y", localtime()),
        "time": strftime("%I:%M %p", localtime())
    }
    return render(request, 'time_display/index.html', context)