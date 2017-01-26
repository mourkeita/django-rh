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
    return HttpResponse("<h3>Hello, world. Welcome to RH QA app.</h3><p><h4>C'est quoi les objectifs de la QA ? </h4>")

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


@csrf_exempt 
def login(request):
    if len(request.POST) > 0:
        if 'email' not in request.POST or 'password' not in request.POST:
            error = 'Veuillez entrer un email et un mot de passe'
            return render_to_response('login.html', {'error':error})
        else:
            email = request.POST['email']
            password = request.POST['password']
            if email != 'test@test.fr' or password != 'test':
                error = u'Mot de passe ou email errone'
		return render_to_response('login.html', {'error':error})
            else:
               return HttpResponseRedirect('/listUsers')
    else:
        return render_to_response('login.html')

def newuser(request):
    form = QaForm()
    return render(request, 'new_user.html', {'form':form})
    if request.method == 'POST':
        form = QaForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            #post.save()
            post.save()
            return redirect('/userdetails')
    else:
        form = QaForm()
    return render(request, 'new_user.html', {'form': form})

def userdetails(request):
    post = request.POST
    return render(request, 'user_details.html', {'post':post} )