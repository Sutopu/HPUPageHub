from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UploadFileForm
from .models import StudentWebPage
from django.core.files.storage import FileSystemStorage

def home(request):
    pages = StudentWebPage.objects.all()
    return render(request, 'hub/hub.html', {'pages':pages})


def page(request, pageURL):
    return render(request, 'hub/page.html', {'pageURL':pageURL})

def upload(request):
    if request.method == "POST":
        #why does this form take the POST part of the requset and the files?
        #this form is a custom form that also counts as a model so it's easy to save form content to the database! huge!
        form = UploadFileForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            #just taking HTML and saving it and letting other users 
            #run it on their browsers is a huge security risk, obviously.
            #not sure if possible to make html safe, but there are some possible solutions/
            #ways to mitigate risk:
            #1. have an administrator look through each HTML file and manually verify that it is safe. 
            #2. parse each uploaded HTML file don't accept files that have tags that aren't allowed
            #3. need to ensure that only html files can be uploaded.
            form.save()
            return redirect('hub:home')
        else:
            #optimally should have a toast pop up if this ever occurs
            return HttpResponse('invalid form')
    form = UploadFileForm()
    return render(request, 'hub/upload.html', {'form':form})





# Create your views here.
