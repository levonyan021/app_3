from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import *
from .forms import *
from django.core.mail import send_mail, BadHeaderError
# Create your views here.

def index(request):
    persons = Image.objects.order_by('-title')
    context = {'persons': persons}
    return render(request, "main/index.html", context=context)

def about(requset):
    persons = Image.objects.order_by('-title')
    context = {'persons': persons}
    return render(requset, "main/about.html", context=context)

def home(request):
    return redirect("http://localhost:8000/home/")

def service(request):
    return render(request, "main/service.html")

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
                'full_name': form.cleaned_data['full_name'],
                'email_address': form.cleaned_data['email_address'],
                'subject': form.cleaned_data['subject'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'eriklevonyan0@gmail.com', ['eriklevonyan0@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return redirect("http://localhost:8000/home/")
    form = ContactForm()
    return render(request, "main/contact.html", {'form': form})