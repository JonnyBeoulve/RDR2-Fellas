from django.shortcuts import render
from rdr2_fellas.forms import UserForm, UserProfileForm
from rdr2_fellas.models import UserProfile
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

# Grab a list of users and redirect to partner page
def partner(request):
    partner_list = UserProfile.objects.order_by('gaming_id')
    partner_dict = {'partners':partner_list}
    return render(request, 'partner.html', context=partner_dict)

# Perform logout for user session
@login_required
def user_logout(request):
    logout(request)
    return render(request, 'logout.html')

# Process login request / render login page
def user_login(request):

    if request.method == 'POST':

        # Grab form values
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("Account not active.")
        else:
            return HttpResponse("Login failed.")

    else:
        return render(request, 'login.html', {})

# Process registration request / render register page and form
def user_register(request):

    registered = False

    if request.method == 'POST':

        # Grab form data
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # Confirm form validity
        if user_form.is_valid() and profile_form.is_valid():

            # Set user, hash password, and then save to database
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            # Set profile, create relationship, then save to database
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            # User is now registered.
            registered = True

        else:
            # Print form invalid
            print(user_form.errors, profile_form.errors)

    else:
        # Render forms
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'register.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})
