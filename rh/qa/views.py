from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from qa.models import Qa
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect

from .forms import QaForm

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponseRedirect("/login")

def listUsers(request):
    users = Qa.objects.all().order_by('id')
    total_age = 0
    for user in users:
        total_age = total_age + user.age

    context = {'users':users, 'total_age':total_age}
    #context2 = {'total_age':total_age}
    return render(request, 'qa.html', context )

def texte(request):
     HttpResponse("<h3>Hello this is a test</h3>")

def newuser(request):
    form = QaForm()
    return render(request, 'new_user.html', {'form':form})

    
def userdetails(request):
    post = request.POST
    form = QaForm(post)
    if form.is_valid():
        form.save()
        return render(request, 'user_details.html', {'post':post} )
    else:
        return HttpResponseRedirect('/newuser')

def logout(request):
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
            if email != result.email or password != result.password:
                error = u'Mot de passe ou email errone'
                return render_to_response('login.html', {'error':error})
            else:
               result = Qa.objects.filter(email=email).first()
               nom = result.first
               request.session['username'] = nom.capitalize()
               username = request.session['username']
               return HttpResponseRedirect('/welcome')
    else:
        return render_to_response('login.html')
