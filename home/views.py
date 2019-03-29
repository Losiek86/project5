from django.shortcuts import render
from pupils.models import Pupil

# Create your views here. 
def index(request):
    pupils = Pupil.objects.all()
    return render(request, 'index.html', {"pupils": pupils})