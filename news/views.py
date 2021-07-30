from django.shortcuts import render
from django.http import HttpResponse

from .models import Article

class ArticleObject:
    def __init__(self, key, title, posted_date, text_preview):
        self.key = key
        self.title = title
        self.posted_date = posted_date
        self.text_preview = text_preview

def index(request):
    entryobjects = Article.objects.all()
    num_entries = 0
    for each in entryobjects:
        num_entries += 1


    entry_counter = (num_entries - (1 * 10)) 

    
    
    entries_titles = []
    entries_keys = []

    entry_endcount = entry_counter + 10
    if (entry_counter < 0):
        entry_counter = 0

    while  (entry_counter < entry_endcount) :
        entry_counter += 1

    entry_counter -= 1

    entries = []
    while (entry_counter > (entry_endcount - 10)):
        try:
            this_entry = Article.objects.get(pk=entry_counter)
        except Exception:
            break
        else:
            news_entry = ArticleObject(this_entry.entry, this_entry.title, this_entry.posted_date, this_entry.text_preview)
            entries.append(news_entry)
            entry_counter -= 1
    
    counter = 1
    template_pages = [counter]
    num_entries -= 10

    while num_entries > 0:
        counter += 1
        template_pages.append(counter)
        num_entries -= 10


    return render(request, 'news.html', {'page':template_pages,'entries':entries})

def archives(request, page):
    entryobjects = Article.objects.all()
    num_entries = 0
    for each in entryobjects:
        num_entries += 1


    entry_counter = (num_entries - (page * 10)) 

    
    
    entries_titles = []
    entries_keys = []

    entry_endcount = entry_counter + 10
    if (entry_counter < 0):
        entry_counter = 0

    while  (entry_counter < entry_endcount) :
        entry_counter += 1

    entry_counter -= 1

    entries = []
    while (entry_counter > (entry_endcount - 10)):
        try:
            this_entry = Article.objects.get(pk=entry_counter)
        except Exception:
            break
        else:
            news_entry = ArticleObject(this_entry.entry, this_entry.title, this_entry.posted_date, this_entry.text_preview)
            entries.append(news_entry)
            entry_counter -= 1
    
    counter = 1
    template_pages = [counter]
    num_entries -= 10

    while num_entries > 0:
        counter += 1
        template_pages.append(counter)
        num_entries -= 10


    return render(request, 'news.html', {'page':template_pages,'entries':entries})

def view_post(request, entry):
    this_entry = Article.objects.get(pk=entry)
    this_title = this_entry.title
    this_text = this_entry.text
    this_date = this_entry.posted_date

    return render(request, 'showpost.html', {'title':this_title, 'text':this_text, 'date':this_date})