from django.shortcuts   import render
from django.http        import HttpResponse
from django.template       import loader


# Create your views here.
def say_hello(request):
    return HttpResponse("Hi")

def panel(request):
  template = loader.get_template('panel.html')
  Widok = 'P'
  if Widok == 'A':
    context = {
      'testx': ['b','c','d','e','f'],
      'active': 'c'}
  if Widok == 'L':
    context = {
      'testx': ['a','c','d','e','f'],
      'active': 'b'}
  if Widok == 'P':
    context = {
      'testx': ['a','b','c','e','f'],
      'active': 'c'}
  return HttpResponse(template.render(context, request))

def test(request):
    return render(request, 'newtest.html')