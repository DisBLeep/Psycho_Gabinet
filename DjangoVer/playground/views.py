from django.shortcuts   import render
from django.http        import HttpResponse
from django.template       import loader


# Create your views here.
def say_hello(request):
    return HttpResponse("Hi")

def panel(request):
  template = loader.get_template('panel.html')
  context = {
    'testx': 'Linus',
  }
  return HttpResponse(template.render(context, request))

def test(request):
    return render(request, 'newtest.html')