from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Switches
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import JsonResponse


def loginpage(request):
    
    
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('pass')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.info(request, 'Welcome')
            return redirect('/')
        else:

            messages.info(request, 'Invalid username or password')
            return render(request, 'login.html')
    
            
    return render(request, 'login.html')

def logoutpage(request):    
    logout(request)
    return redirect('/')

@login_required(login_url='login/')
def main(request):
        
    if request.method == 'GET':
        
        
        if(request.GET.get("switch")):
        
            state,switch =request.GET.get("state"),request.GET.get("switch")
            
            if state == "True":
                switch  = Switches.objects.get(name=switch)
                switch.state = True 
                switch.save()
            else:
                switch  = Switches.objects.get(name=switch)
                switch.state = False 
                switch.save()

    allswitches = Switches.objects.all()
    state  = Switches.objects.get(name="one").state
    state2 = Switches.objects.get(name="two").state
    

    return render(request, 'index.html',context={'state':state,'switches': allswitches,'state2':state2})
 
def jsondump(request):
    allswitches = Switches.objects.all()
    data = serializers.serialize("jsonl", allswitches)
    
    return HttpResponse(data,content_type='application/json')