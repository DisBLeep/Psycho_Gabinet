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

#VERY DIRTY to nie tak że nie było chęci, chęci było mnóstwo, czas zstał zadedykowany.
#Pojęcia mi brak jak w tym loader.get_template podawać względnie relatywne, AAAAAAAAAAAAAAAAAAAA

def panel_pacj2(request):
    template = loader.get_template('pacj.html')
    return HttpResponse(template.render({},request))
def panel_czat2(request):
    template = loader.get_template('czat.html')
    return HttpResponse(template.render({},request))
def panel_info2(request):
    template = loader.get_template('info.html')
    return HttpResponse(template.render({},request))
def panel_kale2(request):
    template = loader.get_template('kale.html')
    return HttpResponse(template.render({},request))
def panel_cnnk2(request):
    template = loader.get_template('cnnk.html')
    return HttpResponse(template.render({},request))
def panel_sttg2(request):
    template = loader.get_template('sttg.html')
    return HttpResponse(template.render({},request))
def panel_wizt2(request):
    template = loader.get_template('wizt.html')
    return HttpResponse(template.render({},request))