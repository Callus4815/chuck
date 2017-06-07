from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

import requests
import json

# Create your views here.


def index(request):
    call = requests.get("https://api.icndb.com/jokes/random/1?firstName=Patrick&lastName=Cox&limitTo=[explicit]")
    called = call.text
    parsed = json.loads(called)
    told = parsed['value'][0]['joke']
    template = loader.get_template('joketeller/index.html')
    context = {
            'joke':told,
                }
    return HttpResponse(template.render(context, request))
