from django.shortcuts import render, get_object_or_404
from .models import Exhibit

def index(request):
    exhibits = Exhibit.objects.all()
    return render(request, 'index.html', {'exhibits': exhibits})

def about(request):
    return render(request, 'about.html')

def floor(request, floor):
    exhibits = Exhibit.objects.filter(floor=floor, is_open=True)
    return render(request, 'floor.html', {'exhibits': exhibits, 'floor': floor})

def exhibit_detail(request, id):
    exhibit = get_object_or_404(Exhibit, id=id)
    return render(request, 'exhibit_detail.html', {'exhibit': exhibit})

from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import redirect
from .models import Exhibit, ExhibitItem
from .forms import ExhibitForm, ExhibitItemForm

def is_staff_user(user):
    return user.is_authenticated and user.is_staff

@login_required
def add_exhibit(request):
    if request.method == "POST":
        form = ExhibitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ExhibitForm()
    return render(request, 'add_exhibit.html', {'form': form})

@login_required
def edit_exhibit(request, id):
    exhibit = get_object_or_404(Exhibit, id=id)
    if request.method == "POST":
        form = ExhibitForm(request.POST, instance=exhibit)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ExhibitForm(instance=exhibit)
    return render(request, 'edit_exhibit.html', {'form': form, 'exhibit': exhibit})