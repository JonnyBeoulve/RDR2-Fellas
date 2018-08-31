from django.shortcuts import render
from rdr2_fellas.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Root page
def home(request):
    return render(request,'index.html')

# About page
def about(request):
    return render(request, 'about.html')

# Partner up page
def partner(request):
    return render(request, 'partner.html')

# Process login request / render login page
def user_login(request):

    if request.method == 'POST':

        # Grab form values
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate
        user = authenticate(email=email, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("Account not active.")
        else:
            print("Login failed.")
            return HttpResponse("Login failed.")

    else:
        return render(request, 'login.html', {})

# Process registration request / render register page and form
def user_register(request):

    registered = False

    if request.method == 'POST':

        # Coming soon...
        print('Working')

    else:
        # Render forms
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'register.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})