from django.shortcuts import render
from .models import Note

def index(request):
    return render(request, 'notes/index.html')

def note_list(request):
    notes = Note.objects.all()
    return render(request, 'notes/note_list.html', {'notes': notes})