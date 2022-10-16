
from django.http import HttpResponse
from django.template import loader
from .models import User
from django.contrib import messages
from django.shortcuts import render, redirect



def index(request):
    if request.method == 'POST':
        user_form = User(request.POST)
        print(user_form)
        if user_form.is_valid():
            messages.success(request, user_form)
        else:
            messages.error(request, 'Error saving form')
        return render(request=request,template_name='start_page.html',context={"username":user[0]['username'],'credit' : user[0]['credit']})

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