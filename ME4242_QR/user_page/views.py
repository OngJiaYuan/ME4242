
from django.http import HttpResponse
from django.template import loader
from .models import User
from django.contrib import messages
from django.shortcuts import render, redirect
import json



def index(request):
    if request.method == 'POST':
        user_form = request.POST
        usernames = user_form.get('username','0')
        print(usernames)
        try:
            userdict = User.objects.get(username=usernames)
            
        except:
            userdict = User(username=usernames,credit=0)
            userdict.save()
        
        return render(request=request,template_name='start_page.html',context={"username":userdict.username,'credit' : userdict.credit})

    user_form = User()
    user = User.objects.all().values()
    return render(request=request,template_name='login_page.html')

def index3(request):
    mymembers = User.objects.all().values()
    print(mymembers)
    template = loader.get_template('start_page.html')
    context = {
        'username': mymembers[0]['username'],
        'credit' : mymembers[0]['credit'],
    }
    return HttpResponse(template.render(context, request))

def index2(request):
    template = loader.get_template('game_page.html')
    return HttpResponse(template.render())