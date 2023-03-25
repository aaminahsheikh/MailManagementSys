from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . models import *

from . forms import IncomingMailForm, OutgoingMailForm
from . filters import IncomingMailFilter, OutgoingMailFilter
from datetime import datetime, timedelta

# Create your views here.

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        
    context = {}
    return render(request, 'mails/login.html', context)

def logout_user(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def dashboard(request):
    incoming = IncomingMail.objects.all()
    outgoing = OutgoingMail.objects.all()

    # Count
    incoming_total = incoming.count()
    outgoing_total = outgoing.count()
    total_record = incoming_total + outgoing_total

    # Today's records.
    todays_in = IncomingMail.objects.filter(date_created__gte=datetime.now() - timedelta(days=1))
    #todays = IncomingMail.objects.filter(date_created__date=datetime.date.today())
    todays_out = OutgoingMail.objects.filter(date_created__gte=datetime.now() - timedelta(days=1))
    
    todays_out_total = todays_out.count()
    todays_in_total = todays_in.count()

    context = {'incoming': incoming, 'outgoing': outgoing,
            'incoming_total': incoming_total, 'outgoing_total': outgoing_total,
            'todays_in': todays_in, 'todays_out': todays_out,
            'total_record': total_record, 'todays_out_total': todays_out_total,
            'todays_in_total': todays_in_total}
    return render(request, 'mails/dashboard.html', context)


@login_required(login_url='login')
def incoming(request):
    all_incoming = IncomingMail.objects.all()
    
    myFilter = IncomingMailFilter(request.GET, queryset=all_incoming)
    all_incoming = myFilter.qs

    context = {'all_incoming': all_incoming, 'myFilter': myFilter}
    return render(request, 'mails/incoming.html', context)


@login_required(login_url='login')
def incoming_form(request):
    user = request.user
    form = IncomingMailForm(initial={'customer': user})

    if request.method == 'POST':
        form = IncomingMailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('incoming')

    context = {'form': form}
    return render(request, 'mails/incoming_form.html', context)


@login_required(login_url='login')
def incoming_form_update(request, pk):
    record = IncomingMail.objects.get(id=pk)    # get by ID
    form = IncomingMailForm(instance=record)

    if request.method == 'POST':
        form = IncomingMailForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('incoming')

    context = {'form': form}
    return render(request, 'mails/incoming_form.html', context)


@login_required(login_url='login')
def incoming_form_delete(request, pk):
    record = IncomingMail.objects.get(id=pk)

    if request.method == 'POST':
        record.delete()
        return redirect('incoming')
    
    context = {'record': record}
    return render(request, 'mails/incoming_delete.html', context)


@login_required(login_url='login')
def outgoing(request):
    all_outgoing = OutgoingMail.objects.all()

    myFilter = OutgoingMailFilter(request.GET, queryset=all_outgoing)
    all_outgoing = myFilter.qs

    context = {'all_outgoing': all_outgoing, 'myFilter': myFilter}
    return render(request, 'mails/outgoing.html', context)


@login_required(login_url='login')
def outgoing_form(request):
    user = request.user
    form = OutgoingMailForm(initial={'customer': user})

    if request.method == 'POST':
        form = OutgoingMailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('outgoing')

    context = {'form': form}
    return render(request, 'mails/outgoing_form.html', context)


@login_required(login_url='login')
def outgoing_form_update(request, pk):
    record = OutgoingMail.objects.get(id=pk)
    form = OutgoingMailForm(instance=record)

    if request.method == 'POST':
        form = OutgoingMailForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('outgoing')
    
    context = {'form': form}
    return render(request, 'mails/outgoing_form.html', context)


@login_required(login_url='login')    
def outgoing_form_delete(request, pk):
    record = OutgoingMail.objects.get(id=pk)
    
    if request.method == 'POST':
        record.delete()
        return redirect('outgoing')
    
    context = {'record': record}
    return render(request, 'mails/outgoing_delete.html', context)