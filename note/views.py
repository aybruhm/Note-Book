from django.shortcuts import render, HttpResponseRedirect, redirect
from .models import Note


def home(request):
    notes = Note.objects.all().order_by('-timestamp')
    return render(request, 'note/index.html', {'notes': notes})

def new(request):
    if request.method == 'POST':
        if request.POST.get('title') and request.POST.get('content') and request.POST.get('optradio'):
            note = Note()
            note.title = request.POST.get('title')
            note.content = request.POST.get('content')
            note.category = request.POST.get('optradio')
            note.save()
            return redirect('')
        else:
            request.method == 'POST'
    return render(request, 'note/new.html')

def note(request, pk):
    _note = Note.objects.get(pk=pk)
    content = _note.content
    print(content)
    return render(request, 'note/note.html', {'content': content})

def update(request, pk):
    pass

def delete(request, pk):
    pass