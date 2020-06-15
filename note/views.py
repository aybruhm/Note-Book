from django.shortcuts import render


def home(request):
    return render(request, 'note/index.html')

def new(request):
    return render(request, 'note/new.html')

def note(request):
    return render(request, 'note/note.html')