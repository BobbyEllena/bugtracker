from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

from bug.models import CustUser
from bug.models import BugModel
from bug.forms import BugForm
from bug.forms import LoginForm


user = get_user_model()
# Create your views here.
def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse('homepage')))

    form = LoginForm()
    return render(request, 'bug_form.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@ login_required
def home_view(request):
    new = BugModel.objects.filter(status='NO').order_by('-time_created')
    in_progress = BugModel.objects.filter(status='IP').order_by('-time_created')
    done = BugModel.objects.filter(status='DO').order_by('-time_created')
    invalid = BugModel.objects.filter(status='IV').order_by('-time_created')
    return render(request, 'homepage.html', {'user': user, 'new': new, 'in_progress': in_progress, 'done': done, 'invalid': invalid})

@ login_required
def bug_view(request, id):
    bug = BugModel.objects.get(id=id)
    return render(request, 'bug_detail.html', {'bug': bug})

@ login_required
def user_view(request, id):
    user = CustUser.objects.get(id=id)
    assigned = BugModel.objects.filter(owner=id).order_by('-time_created')
    filed = BugModel.objects.filter(author=id).order_by('-time_created')
    completed = BugModel.objects.filter(closer=id).order_by('-time_created')
    return render(request, 'user_detail.html', {'user': user, 'assigned': assigned,
                    'filed': filed, 'completed': completed})

@login_required
def addbug_view(request):

    if request.method == 'POST':
        form = BugForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            BugModel.objects.create(
                title=data['title'],
                description=data['description'],
                author=request.user,
                status='NO'
            )
            return HttpResponseRedirect(reverse('homepage'))

    form = BugForm()
    return render(request, 'bug_form.html', {"form": form})

@login_required
def assigntome_view(request, id):
    bug = BugModel.objects.get(id=id)
    bug.status = 'IP'
    bug.owner = request.user
    bug.closer = None
    bug.save()
    return HttpResponseRedirect(reverse('bug', kwargs={'id': id}))

@login_required
def markdone_view(request, id):
    bug = BugModel.objects.get(id=id)
    bug.status = 'DO'
    bug.closer = request.user
    bug.owner = None
    bug.save()
    return HttpResponseRedirect(reverse('bug', kwargs={'id': id}))

@login_required
def markinvalid_view(request, id):
    bug = BugModel.objects.get(id=id)
    bug.status = 'IV'
    bug.closer = None
    bug.owner = None
    bug.save()
    return HttpResponseRedirect(reverse('bug', kwargs={'id': id}))

@login_required
def editbug_view(request, id):
    bug = BugModel.objects.get(id=id)
    if request.method == 'POST':
        form = BugForm(request.POST, instance=bug)
        form.save()
        return HttpResponseRedirect(reverse('bug', args=(id,)))

    form = BugForm(instance=bug)
    return render(request, "bug_form.html", {'form': form})