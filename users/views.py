from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

# Root page
def home(request):
    return render(request,'index.html')

# Login page
def login(request):
    return render(request,'login.html')