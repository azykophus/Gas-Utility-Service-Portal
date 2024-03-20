from django.shortcuts import render, redirect
from .models import ServiceRequest
from django.contrib.auth.forms import UserCreationForm
from .forms import ServiceRequestForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


# services/views.py
from django.shortcuts import render, redirect

def home(request):
    return render(request, 'services/home.html')  # Ensure you have a home.html template


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
       
    else:
        # Handle GET request
        return render(request, 'registration/login.html')
    

@login_required
def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.user = request.user
            service_request.save()
            return redirect('home')
    else:
        form = ServiceRequestForm()
    return render(request, 'services/submit_request.html', {'form': form})

@login_required
def track_requests(request):
    requests = ServiceRequest.objects.filter(user=request.user)
    return render(request, 'services/track_requests.html', {'requests': requests})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect

def login_request(request):
    if request.method == 'POST':
        # Get the username and password from the POST request
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's authenticate method to verify credentials
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # If user credentials are correct, log the user in
            login(request, user)
            # Redirect to a success page.
            return redirect('home')  # Adjust the redirect as needed
        else:
            # Return an 'invalid login' error message.
            return render(request, 'login.html', {'error': 'Invalid username or password.'})
    else:
        # For a GET request, just display the login page
        return render(request, 'login.html')

@login_required
def home_view(request):
    return render(request, '/serviceshome.html')  # Path to your home page template

def root_redirect(request):
    if request.user.is_authenticated:
        return redirect('home')  # Name of the URL pattern for your home page
    else:
        return redirect('login')
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm



def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to home after successful signup
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


