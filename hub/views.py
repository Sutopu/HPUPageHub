from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UploadFileForm
from .models import StudentWebPage
from django.core.files.storage import FileSystemStorage

def home(request):
    #user selected file to upload and clicked submit
    if request.method == 'POST':
        #why does this form take the POST part of the requset and the files?
        #this form is a custom form that also counts as a model so it's easy to save form content to the database! huge!
        form = UploadFileForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
        else:
            return HttpResponse('invalid form')
    else:
        form = UploadFileForm()
        pages = StudentWebPage.objects.all()
        return render(request, 'hub/hub.html', {'form':form, 'pages':pages})




# Create your views here.
