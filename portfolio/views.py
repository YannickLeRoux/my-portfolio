from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.views.generic import TemplateView

class Home(TemplateView):
    template_name = 'portfolio/index.html'

class Contact(TemplateView):
    template_name = 'portfolio/contact.html'

class Blog(TemplateView):
    template_name = 'portfolio/blog.html'

class Portfolio(TemplateView):
    template_name = 'portfolio/portfolio.html'

class About(TemplateView):
    template_name = 'portfolio/about.html'

def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(name, message, from_email,
                        ['yannick.leroux971@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('portfolio:success')
    return render(request, "portfolio/contact.html", {'form': form})

def successView(request):
    return render(request, "portfolio/success.html")
