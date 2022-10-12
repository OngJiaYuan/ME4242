
from django.http import HttpResponse
from django.template import loader
from .models import User

def index(request):
    template = loader.get_template('login_page.html')
    return HttpResponse(template.render())

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