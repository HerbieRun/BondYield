from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')


def bond(request):

	R2list=[{'name':'CHE','value':0.9},
	{'name':'AUG','value':0.8},
	{'name':'CHN','value':0.8}];
	return render(request, 'bond.html',{'rlist':R2list});

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

