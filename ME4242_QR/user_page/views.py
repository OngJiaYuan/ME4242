from django.http import HttpResponse
from django.template import loader
from .models import User
from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
import json
from django.http import HttpResponse
context = {}

def index(request):
    if request.method == 'POST':
        user_form = request.POST
        print(user_form)
        usernames = user_form.get('username','0')
        print(usernames)
        try:
            userdict = User.objects.get(username=usernames)
            
        except:
            userdict = User(username=usernames,credit=0)
            userdict.save()

        context['instance'] = userdict

        return index3(request=request)

    user_form = User()
    user = User.objects.all().values()
    return render(request=request,template_name='login_page.html')

def index3(request):
    mymembers = User.objects.all().values()
    print(mymembers)
    print(context)
    
    if request.method == 'POST':
        if 'topUp' in request.POST:
            user_top = request.POST
            amount = user_top.get('topUp','0')
            usernames = user_top.get('username','0')
            userdict = User.objects.get(username=usernames)
            userdict.top_up(amount=int(amount))
            context['instance'] = userdict
            return render(request=request,template_name='start_page.html',context=context)
        
    return render(request=request,template_name='start_page.html',context=context)

def index2(request):
    if request.method == 'POST':
        usernames = json.loads(request.body)
        usernames = usernames['value']
        usernames = usernames['username']
        userdict = User.objects.get(username=usernames)
        userdict.one_play()
        return HttpResponse(status=201)

    return render(request=request,template_name='game_page.html',context=context)

def game_page(request):
    if request.method == 'POST':
        print(context['instance'])
        usernames = context['instance']
        userdict = User.objects.get(username=usernames)
        context['instance'] = userdict
        if 'topUp' in request.POST:
            user_top = request.POST
            amount = user_top.get('topUp','0')
            usernames = user_top.get('username','0')
            userdict = User.objects.get(username=usernames)
            userdict.top_up(amount=int(amount))
            context['instance'] = userdict
            return render(request=request,template_name='start_page.html',context=context)
        return render(request=request,template_name='start_page.html',context=context)
    return render(request=request,template_name='game_page.html',context=context)