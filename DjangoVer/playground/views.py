from django.shortcuts   import render, redirect
from django.http        import HttpResponse, HttpResponseRedirect
from django.template    import loader
from django.contrib.auth.forms import UserCreationForm
from .forms import *
# Create your views here.
#def say_hello(request):
#    return HttpResponse("Hi")

def register(request):
  form = RegisterForm()
  template = loader.get_template('p_rgst.html')

  if request.method == "POST":
      form = RegisterForm(request.POST)
      if form.is_valid():
        form.save()
        panel(request, "A")
  context = {'form':form}
  return HttpResponse(template.render(context, request))

def panel(request, atype):
  template = loader.get_template('panel.html')
  Widok = 'A'
  if Widok == 'A':
    context = {
      'testx': ['b','c','d','e','f'],
      'active': 'c'}
  return HttpResponse(template.render(context, request))