from django.shortcuts import render, HttpResponseRedirect
from .models import Note


def home(request):
    notes = Note.objects.all().order_by('-timestamp')
    return render(request, 'note/index.html', {'notes': notes})

def new(request):
    if request.method == 'POST':
        if request.POST.get('title') and request.POST.get('content'):
            note = Note()
            note.title = request.POST.get('title')
            note.content = request.POST.get('content')
            note.save()
        else:
            request.method == 'POST'
    return render(request, 'note/new.html')

def note(request, pk):
    context = Note.objects.filter(id=pk)
    note = Note.objects.filter()
    print(note)
    content = note.content(instance=note)
    print(content)
    return render(request, 'note/note.html', {'context': context, 'content': content})

def update(request, pk):
    pass

def delete(request, pk):
    pass