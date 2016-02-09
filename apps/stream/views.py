from django.shortcuts import render, redirect
from .models import AudioFile

# Create your views here.
def stream(request):   
    if not request.user.is_authenticated():
        return redirect('/')
    else:
        files = AudioFile.objects.all()
        print files
        return render(request, 'stream/stream.html', {'data': files})
