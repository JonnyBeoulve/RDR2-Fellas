from django.shortcuts import render
from rdr2_fellas.forms import UserForm, UserProfileForm, UpdateUserProfileForm
from rdr2_fellas.models import UserProfile
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def home(request):
    """ This view directs the user to index.html """

    return render(request,'index.html')

def about(request):
    """ This view direct the user to about.html """

    return render(request, 'about.html')

def partner(request):
    """ This view grabs a list of users and redirects to partner page """

    partner_list = UserProfile.objects.order_by('gaming_id')
    partner_dict = {'partners':partner_list}
    return render(request, 'partner.html', context=partner_dict)

def my_profile(request):
    """ This view lets a user view the information and change it """

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
        my_profile_form = UpdateUserProfileForm()

    return render(request, 'myprofile.html',
                          {'my_profile_form':my_profile_form})


@login_required
def user_logout(request):
    """ This view logs a user out """

    logout(request)
    return render(request, 'logout.html')

def user_login(request):
    """ This view processes a login request or renders login.html """
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('home'))

    if request.method == 'POST':

        # Grab form values
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('partner'))
            else:
                return HttpResponse("Account not active.")
        else:
            return HttpResponse("Login failed.")

    else:
        return render(request, 'login.html', {})

def user_register(request):
    """ This view processes registration request or renders register page """

    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('home'))

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
