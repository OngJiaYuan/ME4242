
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('start_page.html')
    return HttpResponse(template.render())

def index2(request):
    template = loader.get_template('game_page.html')
    return HttpResponse(template.render())