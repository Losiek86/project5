from django.shortcuts import render, redirect, reverse
from .models import Donate

# Create your views here.

    
def donations(request):
    donation = Donate.objects.all()
    return render(request, "donate.html", {"donation": donation})
    
def in_progres(request):
    return render(request, "inprogres.html")
