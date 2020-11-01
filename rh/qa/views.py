# coding: utf-8

import json

from django.contrib.auth import authenticate
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from qa.models import Employee, Company #, JobOffer
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.core.files.storage import FileSystemStorage

from .forms import EmployeeForm

# Create your views here.

from django.http import HttpResponse


def index(request):
    # all_job_offers = list(JobOffer.objects.all())
    # context = {'all_job_offers': all_job_offers}
    # return render_to_response('index.html', context)
    return render_to_response('index.html')

def companies(request):
    if 'logged_user_id' in request.session:
        companies = Company.objects.all()
        username = request.session['username']
        context = {'username':username, 'companies':companies}
        return render(request, 'companies.html', context )
    else:
        return HttpResponseRedirect("/login")

def articles(request):
    if 'logged_user_id' in request.session:
        username = request.session['username']
        context = {'username':username}
        return render(request, 'articles.html', context )
    else:
        return HttpResponseRedirect("/login")

def users(request):
    if 'logged_user_id' in request.session:
        username = request.session['username']
        users = Employee.objects.all()
        total_age = 0
        for user in users:
            total_age = total_age + user.age

        context = {'users':users, 'total_age':total_age, 'username':username}
        return render(request, 'qa.html', context )
    else:
        return HttpResponseRedirect("/login")


def error_page(request):
    return HttpResponse("Login first")


def newuser(request):
    form = EmployeeForm()
    message = '*Erreur. Email existant.'
    return render(request, 'new_user.html', {'form':form}, {'message':message})


def delete(request):
    '''
    Get the user id
    delete it from database
    '''

    users = Employee.objects.all()
    ident = request.POST['id']
    user = Employee.objects.filter(id=ident).first()
    if request.method=='POST':
        user.delete()
        return redirect('/users')
    return render(request, 'users', {'object':user})


def delete_company(request):
    '''
    Get the company id
    delete it from database
    '''
    #import pdb; pdb.set_trace()
    companies = Company.objects.all()
    ident = request.POST['id']
    company = Company.objects.filter(id=ident).first()
    if request.method=='POST':
        company.delete()
        return redirect('/companies')
    return render(request, 'company', {'object':company})

def display_company(request):
    '''
    Get the company id
    delete it from database
    '''
    #import pdb; pdb.set_trace()
    companies = Company.objects.all()
    ident = request.POST['id']
    company = Company.objects.filter(id=ident).first()
    return render(request, 'display_company.html', {'object':company})


def displayuser(request):
    if 'logged_user_id' in request.session:
        username = request.session['username']
        id = request.POST['id']
        user = Employee.objects.filter(id=id).first()
        return render(request, 'display_user.html', {'post': user, 'username':username})
    else:
        return HttpResponseRedirect("/login")

def update(request):
    if 'logged_user_id' in request.session:
        username = request.session['username']
        id = request.POST['id']
        user = Employee.objects.filter(id=id).first()
        return render(request, 'update.html', {'post': user, 'username':username})
    else:
        return HttpResponseRedirect("/login")

def userdetails(request):
    if 'logged_user_id' in request.session:
        username = request.session['username']
        avatar = request.FILES['avatar']
        fs = FileSystemStorage()
        avatar_name = fs.save(str(request.POST['first']).lower()+'-'+str(request.POST['last']).lower()+'.jpg', avatar)

        avatar_url = fs.url(avatar_name)
        post = request.POST
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'user_details.html', {'post':post, 'avatar_url':avatar_url, 'username':username} )
        else:
            return HttpResponseRedirect('/newuser')
    else:
        return HttpResponseRedirect("/login")

def logout(request):
    if 'logged_user_id' in request.session:
        request.session['username'] = ''
        request.session.flush()
        return render_to_response('logout.html')
    else:
        return render_to_response('logout.html', {'deja': 'déjà'})

def welcome(request):
    if 'logged_user_id' in request.session:
        id = request.session['logged_user_id']
        username = request.session['username']
        return render_to_response('welcome.html', {'id':id, 'username':username})
    else:
        return HttpResponseRedirect('/login')

@csrf_exempt
def login(request):
    if len(request.POST) > 0:
         if 'email' not in request.POST or 'password' not in request.POST:
             error = 'Veuillez entrer un email et un mot de passe'
             return render_to_response('login.html', {'error':error})
         else:
             email = request.POST['email']
             password = request.POST['password']
             user = Employee.objects.filter(email=email).first()
             if not user or email != user.email or password != user.password:
                 error = u'Mot de passe ou email erroné'
                 return render_to_response('login.html', {'error':error})
             else:
                user = Employee.objects.filter(email=email).first()
                request.session['username'] = user.first
                request.session['logged_user_id'] = user.id
                username = request.session['username']
                return render_to_response('welcome.html', {'username':username, 'id':user.id})
    else:
        return render_to_response('login.html')

@csrf_exempt
def get_all(request):
    if request.method == 'GET':
        users = Employee.objects.all().values()
        users_list = list(users)
    if request.method == 'POST':    
        body = json.loads(request.body)
        first = body['first']
        last = body['last']
        email = body['email']
        password = body['password']
        age = body['age']
        user = Employee(first=first, last=last, email=email, password=password, age=age)
        user.save()
        return HttpResponse(json.dumps(request.body), content_type='application/json')

    return JsonResponse(users_list, safe=False)


