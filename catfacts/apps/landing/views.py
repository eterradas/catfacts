from django.shortcuts import render_to_response, HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.core.context_processors import csrf
from django.db import IntegrityError, transaction
from django.core.exceptions import ValidationError

from catfacts.apps.landing.models import Recipient
from catfacts.apps.landing.forms import RecipientForm

def add_recipient(request):
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        form = RecipientForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            recipient = Recipient(number=cleaned_data['number'])
            recipient.save()
            recipient.start_catfacts()
            return HttpResponseRedirect('/thanks')
    else:
        form = RecipientForm()
    c['form'] = form
    return render_to_response('home.html', c)

def thanks(request):
    c={}
    return render_to_response('thanks.html',c)