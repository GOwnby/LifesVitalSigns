from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from .forms import SearchForm
from forum.models import Account
from .models import ProfileKey

def index(request):

    if request.method == 'GET':
        form = SearchForm(request.GET)

        if form.is_valid():
            username = form.cleaned_data['username']
            try:
                user = ProfileKey.objects.get(pk = username)
            except BaseException:
                return HttpResponse('User could not be found')

                return render(request, 'searchresults/searchresults.html', {'names':related})
            else:
                return render(request, 'searchresults/searchresults.html', {'user':username})
    
    return HttpResponseRedirect('/forum/')
