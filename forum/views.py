from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from . import forms as myForms
from . import models as myModels
from searchaccount.models import ProfileKey
from searchaccount.forms import SearchForm
import uuid

class ForumObject:
    def __init__(self, key, title, author, dateposted):
        self.key = key
        self.title = title
        self.author = author
        self.dateposted = dateposted

def index(request):
    form = SearchForm()

    if not(request.COOKIES.get('user', 'default') == 'default'):
        user = request.COOKIES.get('user')
        uuid = request.COOKIES.get('uuid')
        userDB_uuid = (myModels.Account.objects.get(pk=(ProfileKey.objects.get(pk=(user))).email)).uuid
        if uuid == userDB_uuid:
            return render(request, 'forum/personalhome.html', {'form':form, 'user':user})

    return render(request, 'forum/home.html', {'form':form})

def climate_science(request, page):

    entryobjects = myModels.ClimateScienceEntry.objects.all()
    num_entries = 0
    for _ in entryobjects:
        num_entries += 1


    entry_counter = (num_entries - (page * 10)) 

    entry_endcount = entry_counter + 10
    if (entry_counter < 0):
        entry_counter = 0

    while  (entry_counter < entry_endcount) :
        entry_counter += 1

    entry_counter -= 1

    entries = []
    while (entry_counter > (entry_endcount - 10)):
        try:
            this_entry = myModels.ClimateScienceEntry.objects.get(pk=entry_counter)
        except BaseException:
            break
        else:
            forum_entry = ForumObject(this_entry.entry, this_entry.title, this_entry.posted_by, this_entry.posted_date)
            entries.append(forum_entry)
            entry_counter -= 1
    
    counter = 1
    template_pages = [counter]
    num_entries -= 10

    while num_entries > 0:
        counter += 1
        template_pages.append(counter)
        num_entries -= 10


    return render(request, 'forum/ClimateScienceForum.html', {'page':template_pages,'entries':entries})

def climate_science_entry(request, entry):
    this_entry = myModels.ClimateScienceEntry.objects.get(pk=entry)
    this_title = this_entry.title
    this_text = this_entry.text
    this_date = this_entry.posted_date

    return render(request, 'forum/showtopic.html', {'title':this_title, 'text':this_text, 'date':this_date, 'subject':'climatescience', 'subjectname':'Climate Science'})

def environmental_science(request, page):

    entryobjects = myModels.EnvironmentalScienceEntry.objects.all()
    num_entries = 0
    for _ in entryobjects:
        num_entries += 1


    entry_counter = (num_entries - (page * 10)) 

    entry_endcount = entry_counter + 10
    if (entry_counter < 0):
        entry_counter = 0

    while  (entry_counter < entry_endcount) :
        entry_counter += 1

    entry_counter -= 1

    entries = []
    while (entry_counter > (entry_endcount - 10)):
        try:
            this_entry = myModels.EnvironmentalScienceEntry.objects.get(pk=entry_counter)
        except BaseException:
            break
        else:
            forum_entry = ForumObject(this_entry.entry, this_entry.title, this_entry.posted_by, this_entry.posted_date)
            entries.append(forum_entry)
            entry_counter -= 1
    
    counter = 1
    template_pages = [counter]
    num_entries -= 10

    while num_entries > 0:
        counter += 1
        template_pages.append(counter)
        num_entries -= 10


    return render(request, 'forum/EnvironmentalScienceForum.html', {'page':template_pages,'entries':entries})

def environmental_science_entry(request, entry):
    this_entry = myModels.EnvironmentalScienceEntry.objects.get(pk=entry)
    this_title = this_entry.title
    this_text = this_entry.text
    this_date = this_entry.posted_date

    return render(request, 'forum/showtopic.html', {'title':this_title, 'text':this_text, 'date':this_date, 'subject':'environmentalscience', 'subjectname':'Environmental Science'})

def ecology(request, page):

    entryobjects = myModels.EcologyEntry.objects.all()
    num_entries = 0
    for _ in entryobjects:
        num_entries += 1


    entry_counter = (num_entries - (page * 10)) 

    entry_endcount = entry_counter + 10
    if (entry_counter < 0):
        entry_counter = 0

    while  (entry_counter < entry_endcount) :
        entry_counter += 1

    entry_counter -= 1

    entries = []
    while (entry_counter > (entry_endcount - 10)):
        try:
            this_entry = myModels.EcologyEntry.objects.get(pk=entry_counter)
        except BaseException:
            break
        else:
            forum_entry = ForumObject(this_entry.entry, this_entry.title, this_entry.posted_by, this_entry.posted_date)
            entries.append(forum_entry)
            entry_counter -= 1
    
    counter = 1
    template_pages = [counter]
    num_entries -= 10

    while num_entries > 0:
        counter += 1
        template_pages.append(counter)
        num_entries -= 10


    return render(request, 'forum/EcologyForum.html', {'page':template_pages,'entries':entries})

def ecology_entry(request, entry):
    this_entry = myModels.EcologyEntry.objects.get(pk=entry)
    this_title = this_entry.title
    this_text = this_entry.text
    this_date = this_entry.posted_date

    return render(request, 'forum/showtopic.html', {'title':this_title, 'text':this_text, 'date':this_date, 'subject':'ecology', 'subjectname':'Ecology'})

def technology(request, page):

    entryobjects = myModels.TechnologyEntry.objects.all()
    num_entries = 0
    for _ in entryobjects:
        num_entries += 1


    entry_counter = (num_entries - (page * 10)) 

    

    entry_endcount = entry_counter + 10
    if (entry_counter < 0):
        entry_counter = 0

    while  (entry_counter < entry_endcount) :
        entry_counter += 1

    entry_counter -= 1

    entries = []
    while (entry_counter > (entry_endcount - 10)):
        try:
            this_entry = myModels.TechnologyEntry.objects.get(pk=entry_counter)
        except BaseException:
            break
        else:
            forum_entry = ForumObject(this_entry.entry, this_entry.title, this_entry.posted_by, this_entry.posted_date)
            entries.append(forum_entry)
            entry_counter -= 1
        
    counter = 1
    template_pages = [counter]
    num_entries -= 10

    while num_entries > 0:
        counter += 1
        template_pages.append(counter)
        num_entries -= 10


    return render(request, 'forum/TechnologyForum.html', {'page':template_pages, 'entries':entries})

def technology_entry(request, entry):
    this_entry = myModels.TechnologyEntry.objects.get(pk=entry)
    this_title = this_entry.title
    this_text = this_entry.text
    this_date = this_entry.posted_date

    return render(request, 'forum/showtopic.html', {'title':this_title, 'text':this_text, 'date':this_date, 'subject':'technology', 'subjectname':'Technology'})

def add_topic(request, subject):
    
    if not(request.COOKIES.get('user', 'default') == 'default'):
        if request.method == 'POST':
            form = myForms.TopicForm(request.POST)
            if form.is_valid():
                form_title = form.cleaned_data['title']
                form_text = form.cleaned_data['text']
                username = request.COOKIES.get('user')
                counter = 0
            
                if subject == 'climatescience':
                    for _ in myModels.ClimateScienceEntry.objects.all():
                        counter += 1
                    this_entry = myModels.ClimateScienceEntry(title = form_title, text = form_text, entry = counter, posted_by = username)
                    this_entry.save()
                    user = myModels.Account.objects.get(pk=(ProfileKey.objects.get(pk=(username))).email )
                    user.posts += 1
                    user.save()
                    return HttpResponseRedirect('/forum/climatescience/post_' + str(this_entry.entry))

                if subject == 'environmentalscience':
                    for _ in myModels.EnvironmentalScienceEntry.objects.all():
                        counter += 1
                    this_entry = myModels.EnvironmentalScienceEntry(title = form_title, text = form_text, entry = counter, posted_by = username)
                    this_entry.save()
                    user = myModels.Account.objects.get(pk=(ProfileKey.objects.get(pk=(username))).email )
                    user.posts += 1
                    user.save()
                    return HttpResponseRedirect('/forum/environmentalscience/post_' + str(this_entry.entry))
                
                if subject == 'ecology':
                    for _ in myModels.EcologyEntry.objects.all():
                        counter += 1
                    this_entry = myModels.EcologyEntry(title = form_title, text = form_text, entry = counter, posted_by = username)
                    this_entry.save()
                    user = myModels.Account.objects.get(pk=(ProfileKey.objects.get(pk=(username))).email )
                    user.posts += 1
                    user.save()
                    return HttpResponseRedirect('/forum/ecology/post_' + str(this_entry.entry))

                if subject == 'technology':
                    for _ in myModels.TechnologyEntry.objects.all():
                        counter += 1
                    this_entry = myModels.TechnologyEntry(title = form_title, text = form_text, entry = counter, posted_by = username)
                    this_entry.save()
                    user = myModels.Account.objects.get(pk=(ProfileKey.objects.get(pk=(username))).email )
                    user.posts += 1
                    user.save()
                    return HttpResponseRedirect('/forum/technology/post_' + str(this_entry.entry))
            

        else:
            form = myForms.TopicForm()
    else:
        return HttpResponseRedirect('/forum/login/')

    return render(request, 'forum/addtopic.html', {'form':form, 'subject':subject})


def login(request):

    if request.method == 'POST':
        form = myForms.LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                userDB = myModels.Account.objects.get(pk=email)
            except BaseException:
                return HttpResponse('Account does not exist')
            else:
                if userDB.email == email:
                    if userDB.password == password:
                        response = HttpResponseRedirect('/forum/user_' + userDB.username + '/')
                        unique_uuid = uuid.uuid4()
                        response.set_cookie('uuid', unique_uuid)
                        userDB.uuid = unique_uuid
                        userDB.save()
                        response.set_cookie('user', userDB.username)
                        return response
        form = myForms.LoginForm()
    
    return render(request, 'login/login.html', {'form':form})




def create_account(request):

    if request.method == 'POST':
        form = myForms.AccountForm(request.POST)

        if form.is_valid():
            form_username = form.cleaned_data['username']
            form_email = form.cleaned_data['email']
            form_password = form.cleaned_data['password']
            conf_pass = form.cleaned_data['confirm_password']
            if not(conf_pass == form_password):
                return HttpResponse('Passwords do not match')
            unique_uuid = uuid.uuid4()
            new_acc = myModels.Account(username = form_username, email = form_email, password = form_password, uuid = unique_uuid)
            new_acc.save()
            new_user_key = ProfileKey(username = form_username, email = form_email)
            new_user_key.save()
            response = HttpResponseRedirect('/forum/user_' + new_acc.username + '/')
            response.set_cookie('uuid', new_acc.uuid)
            response.set_cookie('user', new_acc.username)
            return response
        return HttpResponse('Bad Request')
    form = myForms.AccountForm()
    return render(request, 'login/createaccount.html', {'form':form})


def profile(request, username):

    profile = myModels.Account.objects.get(pk=(ProfileKey.objects.get(pk=(username))).email )

    requested_uuid = request.COOKIES.get('uuid')

    if profile.uuid == requested_uuid:
        response = render(request, 'forum/personalprofile.html', {'profile':profile})
        response.set_cookie('user', username)
        return response
    
    return render(request, 'forum/profile.html', {'profile':profile})


def logout(request):
    response = HttpResponseRedirect('/forum/')
    response.set_cookie('uuid', 'default')
    response.set_cookie('user', 'default')

    return response