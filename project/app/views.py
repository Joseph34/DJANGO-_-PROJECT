from django.shortcuts import render,redirect
from django.contrib import messages
from app.models import Contact

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method=="POST":
        fname=request.POST.get('name')
        femail=request.POST.get('email')
        fsubject=request.POST.get('subject')
        fmessage=request.POST.get('message')
        query=Contact(name=fname,email=femail,subject=fsubject,message=fmessage)
        query.save()
        messages.success(request, "Thanks for contacting us. We will get by you soon")

        return redirect('/contact')
    return render(request, 'contact.html')

def Announcement(request):
    return render(request, 'announcement.html')

def Announcedet(request):
    return render(request, 'announcement-details.html')