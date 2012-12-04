from django.shortcuts import render_to_response, HttpResponse, HttpResponseRedirect
from django.http import Http404
from landing.models import Recipient
from landing.forms import RecipientForm
from django.core.context_processors import csrf
from django.db import IntegrityError, transaction
from django.core.exceptions import ValidationError
# Create your views here.

def add_recipient(request):
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        form = RecipientForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            r = Recipient(number=cd['number'])
            r.save()
            r.start_catfacts()
            return HttpResponseRedirect('/thanks')
    else:
        form = RecipientForm()
    c['form'] = form
    return render_to_response('home.html', c)

def thanks(request):
    c={}
    return render_to_response('thanks.html',c)