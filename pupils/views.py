from django.shortcuts import render
from pupils.models import Pupil

# Create your views here.

def all_pupils(request):
    pupils = Pupil.objects.all()
    return render(request, "pupils.html", {"pupils": pupils})

def pupil(request, pupil_id):
    pupil = Pupil.objects.get(id=pupil_id)
    return render(request, "pupil.html", {"pupil": pupil})