from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmpresasForm
from .models import Empresas
from tickets.forms import AddTicket
from .calculations import Calculations
from django.http import HttpResponseRedirect
from django.urls import reverse
from users.models import Profile
# Create your views here.
tasks = {"foo", "Bar", "baz"}

context =  {}
my_list = []
#context =  Empresas.objects.get(id=8)



def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    else:
        print('Entering Index Tasks')
        my_list = []
        for i in Empresas.objects.all():
            try:
                my_list.append(i)
                context['my_list'] = my_list
            except:
                print('Except')
        context['page'] = 'DashBoard-1'
        context['list_size'] = len(my_list)
        context['receita_total'] = Calculations().total_valor(my_list)
        context['receita_total'] = Calculations().convert_money(context['receita_total'])
        context['total_pacotes'] = Calculations().total_pacotes(my_list)
        dicionario_empresas_chamadas = {'Rvt': 27, 'Proxer': 25,'Wimax': 13, 'R2': 9, 'Cambuhy': 3, 'Telecall': 8}
        context['empresa_nomes'] = dicionario_empresas_chamadas
        context['empresa_quantidade_chamadas'] = dicionario_empresas_chamadas.values()
        context['total_chamadas'] = Calculations().total_chamadas(dicionario_empresas_chamadas)
        for itens in Profile.objects.all():
             if itens.user == request.user:
                 context['senha'] = itens.user.username
        return render(request, "tasks/index.html",context)
        


def ini_sup(request):
    
    return render(request, "tasks/ini_sup.html")   



def chart(request):
    my_list = []
    for i in Empresas.objects.all():
        try:
            my_list.append(i)
            context['my_list'] = my_list
        except:
            print('Except')
    context['page'] = 'DashBoard-1'
    context['list_size'] = len(my_list)
    context['receita_total'] = Calculations().total_valor(my_list)
    context['receita_total'] = Calculations().convert_money(context['receita_total'])
    context['total_pacotes'] = Calculations().total_pacotes(my_list)
    return render(request, "tasks/chartjs.html",context)  

def add_tickets(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    else:

        form = AddTicket(request.POST or None)
        if form.is_valid():
            form.save()
        context['page'] = 'Ticket'
        context['list_size'] = len(my_list)
        context['form'] = form
        return render(request, "tasks/add_ticket.html",context)

def add_empresas(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    else:

        form = AddTicket(request.POST or None)
        if form.is_valid():
            form.save()
        context['page'] = 'AdicionarEmpresas'
        context['list_size'] = len(my_list)
        context['form'] = form
        return render(request, "tasks/add_empresas.html",context)

def empresas(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    else:

        form = AddTicket(request.POST or None)
        if form.is_valid():
            form.save()
        context['page'] = 'AdicionarEmpresas'
        context['list_size'] = len(my_list)
        context['form'] = form
        return render(request, "tasks/empresas.html",context)
