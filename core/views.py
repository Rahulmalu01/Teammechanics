from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm

def home(request):
    return render(request, 'home.html')

def workshops(request):
    return render(request, 'workshops.html')

def labs(request):
    return render(request, 'labs.html')

def store(request):
    return render(request, 'store.html')

def projects(request):
    return render(request, 'projects.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thankyou')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
