from django.shortcuts import render, HttpResponseRedirect, redirect
from .models import Note
from .forms import NoteForm


def home(request):
    notes = Note.objects.all().order_by('-timestamp')
    return render(request, 'note/index.html', {'notes': notes})

def new(request):
    form = NoteForm()

    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = NoteForm()
            return HttpResponseRedirect("/")
    return render(request, 'note/new.html', {'form': form})

def note(request, pk):
    print(pk)
    note_ = Note.objects.get(pk=pk) # Gets each note
    print(note_.content)
    return render(request, 'note/note.html', {'note_': note_, 'pk': pk})

def update(request, pk):
    note_ = Note.objects.get(pk=pk)
    form = NoteForm(instance=note_)

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note_)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = NoteForm(instance=note_)
    return render(request, 'note/update.html', {'form': form})

def delete(request, pk):
    Note.objects.get(id=pk).delete()
    return HttpResponseRedirect("/")