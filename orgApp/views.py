from django.shortcuts import render
from .models import *
from django.http import HttpRequest, HttpResponsePermanentRedirect
from django.shortcuts import reverse
from orgApp import forms


def home(request):
    context = {
        'Organisations': Organisation.objects.all()
    }
    return render(request, 'orgApp/home.html', context)


def self_org(request: HttpRequest):
    logged_in_user = request.user
    queryset = Organisation.objects.filter(owner_id=logged_in_user)
    new = True if queryset.count() == 0 else None
    context = {'queryset': queryset, 'errorMsg': None, 'new': new}

    # check for request type

    if request.method == 'GET':
        if new:
            form = forms.OrganisationMainRegForm()
            context['orgForm'] = form
        return render(request, 'orgApp/selfOrg.html', context)
    elif request.method == 'POST':
        data = request.POST
        if new:
            form = forms.OrganisationMainRegForm(data)
            if form.is_valid():
                form.save(commit=False)
                form.owner_id = logged_in_user
                form.save()
                return HttpResponsePermanentRedirect(reverse("orgApplication:self_org"))
        context['errorMsg'] = 'Not new user'
        return render(request, 'orgApp/selfOrg.html', context)


