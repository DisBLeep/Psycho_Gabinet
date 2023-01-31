from django.shortcuts import render
from django.shortcuts   import render, redirect
from django.http        import HttpResponse, HttpResponseRedirect
from django.template    import loader
from django.contrib.auth.forms import UserCreationForm
from .forms import *



# Create your views here.
def testd(request):
    return HttpResponse("Hi")

def main(request):
    template = loader.get_template('p_main.html')
    return HttpResponse(template.render({},request))

def rgst(request):
    template = loader.get_template('p_rgst.html')
    return HttpResponse(template.render({},request))

def logn(request):
    template = loader.get_template('p_logn.html')
    return HttpResponse(template.render({},request))

def dev(request):
    template = loader.get_template('p_dev.html')
    return HttpResponse(template.render({},request))

def panel_pacj(request):
    template = loader.get_template('p_panel_spec/pacj.html')
    return HttpResponse(template.render({},request))
def panel_czat(request):
    template = loader.get_template('p_panel_spec/czat.html')
    return HttpResponse(template.render({},request))
def panel_info(request):
    template = loader.get_template('p_panel_spec/info.html')
    return HttpResponse(template.render({},request))
def panel_kale(request):
    template = loader.get_template('p_panel_spec/kale.html')
    return HttpResponse(template.render({},request))
def panel_cnnk(request):
    template = loader.get_template('p_panel_spec/cnnk.html')
    return HttpResponse(template.render({},request))
def panel_sttg(request):
    template = loader.get_template('p_panel_spec/sttg.html')
    return HttpResponse(template.render({},request))
def panel_wizt(request):
    template = loader.get_template('p_panel_spec/wizt.html')
    return HttpResponse(template.render({},request))