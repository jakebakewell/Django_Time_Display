from django.shortcuts import render, redirect
from time import gmtime, strftime
from datetime import datetime

def index(request):
    return redirect("/timedisplay")
def timedisplay(request):
    context = {
        "time_year": strftime("%m-%d-%Y"),
        "time_clock": strftime("%I:%M %p")
    }
    return render(request,'index.html', context)