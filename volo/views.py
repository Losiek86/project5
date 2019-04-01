from django.shortcuts import render
from django.contrib import messages
from .models import Volo
from .forms import VoloForm
from django.template.context_processors import csrf
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

@login_required()
def volo(request):
    if request.method == "POST":
        vf = VoloForm(request.POST)
        if vf.is_valid():
            volo = vf.save(commit=False)
            volo.date = timezone.now()
            volo.save()
            messages.success(request, 'You have successfully applied')
            return HttpResponseRedirect('/volo/')
    else:
        vf = VoloForm()
        
    args = {}
    args.update(csrf(request))
    args['form'] = vf
    
    return render(request, 'volontary.html', args)
    
def check(request):
    volo = Volo.objects.all()
    return render(request, 'check.html', {"volo": volo})
