from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from HRadministrator.models import *
# Create your views here.

@login_required(login_url="/")
def candidate_home(request):
    user = request.user
    return render(request, 'home.html', {'user':user})

@login_required(login_url="/")
def candidate_dashboard(request):
    requi = requisition.objects.all().count
    post = position.objects.all().count
    context = {
        'requi':requi,
        'post':post,
    }
    return render(request, 'candidate_dashboard.html', context)

@login_required(login_url="/")
def candidate_profile(request):
    user = request.user
    return render(request, 'profile.html')

