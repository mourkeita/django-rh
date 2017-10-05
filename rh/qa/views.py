# coding: utf-8

import json

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from qa.models import Qa
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect

from .forms import QaForm

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponseRedirect("/login")

def api(request):
    return render_to_response('api.html')

def listUsers(request):
    users = Qa.objects.all()
    total_age = 0
    name_length = 0
    for user in users:
        name_length = user.first.__sizeof__() + user.last.__sizeof__()
        total_age = total_age + user.age
        print name_length

    context = {'users':users, 'total_age':total_age}
    #context2 = {'total_age':total_age}
    return render(request, 'qa.html', context )

def texte(request):
    HttpResponse("<h3>Hello this is a test</h3>")

def newuser(request):
    form = QaForm()
    message = '*Erreur. Email existant.'
    return render(request, 'new_user.html', {'form':form}, {'message':message})

def delete(request):
    '''
    Get the user id
    delete it from database
    '''
    users = Qa.objects.all()
    ident = request.POST['id']
    user = Qa.objects.filter(id=ident).first()
    if request.method=='POST':
        user.delete()
        return redirect('/listUsers')
    return render(request, 'listUsers', {'object':user})

def userdetails(request):
    post = request.POST
    form = QaForm(post)
    if form.is_valid():
        form.save()
        return render(request, 'user_details.html', {'post':post} )
    else:
        return HttpResponseRedirect('/newuser')

def logout(request):
    request.session['username'] = ''
    return render_to_response('logout.html')

def welcome(request):
    username = request.session['username']
    return render_to_response('welcome.html', {'username':username})

@csrf_exempt 
def login(request):
    username = "not logged in"
    if len(request.POST) > 0:
        if 'email' not in request.POST or 'password' not in request.POST:
            error = 'Veuillez entrer un email et un mot de passe'
            return render_to_response('login.html', {'error':error})
        else:
            email = request.POST['email']
            password = request.POST['password']
            result = Qa.objects.filter(email=email).first()
            if not result or email != result.email or password != result.password:
                error = u'Mot de passe ou email erroné'
                return render_to_response('login.html', {'error':error})
            else:
               result = Qa.objects.filter(email=email).first()
               nom = result.first
               request.session['username'] = nom.capitalize()
               username = request.session['username']
               return HttpResponseRedirect('/welcome')
    else:
        return render_to_response('login.html')

@csrf_exempt
def get_all(request):
    result = []
    if request.method == 'GET':
        users = Qa.objects.all().values()
        users_list = list(users)
    if request.method == 'POST':    
        body = json.loads(request.body)
        first = body['first']
        last = body['last']
        email = body['email']
        password = body['password']
        age = body['age']
        user = Qa(first=first, last=last, email=email, password=password, age=age)
        print user.first
        user.save()
        return HttpResponse(json.dumps(request.body), content_type='application/json')

    return JsonResponse(users_list, safe=False)


