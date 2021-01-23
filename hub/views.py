from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UploadFileForm
from .models import StudentWebPage

def home(request):
    #user selected file to upload and clicked submit
    if request.method == 'POST':
        #why does this form take the POST part of the requset and the files?
        #this form is a custom form that also counts as a model so it's easy to save form content to the database! huge!
        form = UploadFileForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('woooo we did it!')
        else:
            return HttpResponse('invalid')
    else:
        form = UploadFileForm()
        #this is broken currently. I just want a list of all files without title or author. 
        #files = [StudentWebPage.objects.all()[i]["file"] for i in range(len(StudentWebPage.objects.all()))]
    return render(request, 'hub/hub.html', {'form':form, 'files':files})




# Create your views here.
