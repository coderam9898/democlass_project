from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from  .models import demousers,todo,simpletodo
from django.contrib import messages

# Create your views here.
def index(request):
    # template = loader.get_template('templates/index.html')
    template = loader.get_template('home.html')
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

def create(request):
  if request.method == 'POST':
    em = request.POST.get['email']
    newsub = simpletodo(task=em)
    newsub.save()
    success = 'user '+em+' recorded successfuly'
    return HttpResponse('success')


def home(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render({}, request))


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