from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect , JsonResponse
from django.urls import reverse
from  .models import demousers,todo,simpletodo,newuser
from django.contrib import messages

# Create your views here.
def index(request):
    # template = loader.get_template('templates/index.html')
    template = loader.get_template('index.html')
    u = simpletodo.objects.all().values('id','task')
    print(u)
    # return HttpResponse(u)
    context = {
    'data' : u,
    }
    return HttpResponse(template.render(context,request))


def add(request):
    template = loader.get_template('index.html')
    task = ' first todo app fhdfsgkdfb hjgf gdsf '
    if simpletodo.objects.filter(task = task).exists():
       messages.warning(request,'email aready exists')
       print('task already exist')
       return HttpResponse(template.render({},request))
    else:
        t = simpletodo(task=task)
        t.save()
        u = simpletodo.objects.all().values('id','task')
        context = {
        'data' : u,
        }
        return HttpResponse(template.render(context,request))

def creates(request):
  if request.method == 'POST':
    em = request.POST.get['task']
    newsub = simpletodo(task=em)
    newsub.save()
    success = 'user '+em+' recorded successfuly'
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))
  
  
def delete(request, id):
    todo = get_object_or_404(simpletodo, pk=id)
    todo.delete()

    return redirect('index')


def create(request):
    if request.method == 'POST':
        name = request.POST.get('task')
        print(name)
        nuser = simpletodo(task = name)
        nuser.save()
    else:
        print('unspported data')

    # return  HttpResponse('hello world')
    # return HttpResponseRedirect('index')
    return HttpResponseRedirect(reverse('index'))

def home(request):
    template = loader.get_template('index.html')
    u = simpletodo.objects.all().values('id','task')
    print(u)
    # return HttpResponse(u)
    context = {
    'data' : u,
    }
    return HttpResponse(template.render(context,request))
  


def adds(request):
    # e = request.POST['email']
    t = 'some task'
    if simpletodo.objects.filter(task = t).exists():
          messages.warning(request,'email aready exists')
          # return HttpResponse(SUCCESS)
          return HttpResponseRedirect(reverse('demo_app:index'))
         
    else:
          subs = simpletodo(task=t)
          subs.save()
          messages.success(request,'task recorded successfully.')
          return HttpResponseRedirect(reverse('demo_app:index'))


def useradmin(request):
     adminuser = 'Ramkumar Mahato'
     print(adminuser)
     data = {
         'revenue': '400',
         'users': '2k',
         'newuser' : '4k',
         'uptime' : '252',
         'todo': '8',
         'isseus':'23'
     }
     context = {
         'data' : data,
         'admin': adminuser
     }
     template = loader.get_template('admin.html')
     return HttpResponse(template.render(context,request))


def newreg(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone_no')
        address = request.POST.get('address')
        nuser = newuser(name = name, uemail = email, password= password,phone = phone , address = address)
        nuser.save()
    else:
        print('unspported data')

    return  HttpResponse('hello world')

import requests
# Create your views here.
def users(request):
    #pull data from third party rest api
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    #convert reponse data into json
    users = response.json()
    # print(users)
    # return HttpResponse(users)
    return JsonResponse(users,safe=False)