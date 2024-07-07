from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import auth, User
from django.contrib.auth.hashers import make_password

from HRadministrator.models import *


# Create your views here.

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_superuser == True:
                login(request, user)
                return redirect('/HRadministrator/dashboard')
            else:
                login(request, user)
                return redirect('/candidate/dashboard')
        else:
            messages.error(request, 'please check your username and password')
    return render(request, 'login.html')


@login_required(login_url="/")
def logout_user(request):
    auth.logout(request)
    return redirect('/')

@login_required(login_url="/")
def dashboard(request):
    post_count = position.objects.all().count()
    requi_count = requisition.objects.all().count
    cand_count = candidate.objects.all().count()
    context = {
        'post_count':post_count,
        'requi_count':requi_count,
        'cand_count':cand_count,
    }
    return render(request, 'dashboard.html', context)

@login_required(login_url="/")
def homepage(request):
    users = User.objects.all()
    return render(request, 'base.html', {'users':users})

@login_required(login_url="/")
def org_setup(request):
    org = organization.objects.all()
    return render(request, 'Orgsetup/org.html', {'orgs':org})

@login_required(login_url="/")
def create_org(request):
    if request.method == 'POST':
        name = request.POST.get("orgname")
        org = organization.objects.create(name=name)
        org.save()
        return redirect('/HRadministrator/organization')
    return render(request, 'Orgsetup/create_org.html')

@login_required(login_url="/")
def dept_setup(request):
    depts = department.objects.all()
    return render(request, 'DeptSetup/dept.html', {'depts':depts})

@login_required(login_url="/")
def create_dept(request):
    orgs = organization.objects.all()
    if request.method == 'POST':
        name = request.POST.get("deptname")
        orgname = request.POST.get("orgname")
        dept = department.objects.create(name=name, orgname_id=orgname)
        dept.save()
        return redirect('/HRadministrator/department')
    return render(request, 'DeptSetup/create_dept.html', {'orgs':orgs})

@login_required(login_url="/")
def Pos_setup(request):
    posts = position.objects.all()
    return render(request, 'PosSetup/pos.html', {'posts':posts})

@login_required(login_url="/")
def create_pos(request):
    depts = department.objects.all()
    if request.method == 'POST':
        name = request.POST.get("posname")
        orgname = request.POST.get("orgname")
        deptname = request.POST.get("deptname")
        post = position.objects.create(name=name, deptname_id=deptname, orgname_id=orgname)
        post.save()
        return redirect('/HRadministrator/position')
    return render(request, 'PosSetup/create_pos.html', {'depts':depts})

@login_required(login_url="/")
def requi_setup(request):
    requis = requisition.objects.all()
    return render(request, 'RequiSetup/requi.html', {'requis':requis})

@login_required(login_url="/")
def create_requi(request):
    posts = position.objects.all()
    if request.method == 'POST':
        requiid = request.POST.get("requiid")
        post = request.POST.get("post")
        noofopen = request.POST.get("open")
        minsal = request.POST.get("minsal")
        maxsal = request.POST.get("maxsal")
        minexp = request.POST.get("minexp")
        maxexp = request.POST.get("maxexp")
        qualify = request.POST.get("qualify")
        requi = requisition.objects.create(requisition_id=requiid, positionname_id=post, no_of_openings=noofopen, min_salary=minsal, max_salary=maxsal, min_experiance=minexp, max_experiance=maxexp, qualification=qualify)
        requi.save()
        return redirect('/HRadministrator/requisition')
    return render(request, 'RequiSetup/create_requi.html',{'posts':posts})

@login_required(login_url="/")
def cand_setup(request):
    cands = candidate.objects.all()
    return render(request, 'CandSetup/cand.html', {'cands':cands})

@login_required(login_url="/")
def create_cand(request):
    if request.method == 'POST':
        cand_id = request.POST.get("candid")
        first_name = request.POST.get("fname")
        last_name = request.POST.get("lname")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        paswd = make_password(cand_id)
        cand = candidate.objects.create(cand_id=cand_id, first_name=first_name, last_name=last_name, email=email, mobile=mobile)
        cand.save()
        user = User.objects.create(username = cand_id, first_name = first_name, last_name=last_name, email=email, password = paswd)
        user.save()
        return redirect('/HRadministrator/candidate')
    return render(request, 'CandSetup/create_cand.html')

@login_required(login_url="/")
def requi_cand(request, pk):
    requis = requisition.objects.get(pk=pk)
    req_id = requis.id
    cands = candidate.objects.all()
    if request.method == 'POST':
        cand = request.POST.get("cand")
        req_cand = requisition_candidates.objects.create(requisition_id = req_id, candidate_id = cand)
        req_cand.save()
        return redirect("/HRadministrator/requisition")
    return render(request, "RequiSetup/requi_assign_cand.html", {'requis':requis, 'cands':cands})

@login_required(login_url="/")
def assigened_candidates(request, pk):
    requis = requisition.objects.get(pk=pk)
    req_cad = requisition_candidates.objects.filter(requisition=requis)
    return render(request, 'RequiSetup/assignedcad.html', {'req_cads':req_cad})





