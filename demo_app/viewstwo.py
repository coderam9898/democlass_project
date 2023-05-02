from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from  .models import demousers

# Create your views here.
def indextwo(request):
    # template = loader.get_template('templates/index.html')
    template = loader.get_template('index.html')
    u = demousers.objects.all().values()
    # print(u)
    # return HttpResponse(u)
    context = {
    'data' : u,
    }
    return HttpResponse(template.render(context,request))