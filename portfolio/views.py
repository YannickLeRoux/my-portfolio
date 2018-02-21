from django.core.mail import BadHeaderError, EmailMessage
from django.template.loader import render_to_string
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
            to = ['yannick.leroux971@gmail.com']
            subject = "I got a message from yannick-dev"
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                context = {
                        'name': name,
                        'from_email': from_email,
                        'message': message
                        }
                message = render_to_string('portfolio/email/email.txt',
                        context)
                EmailMessage(subject, message, to=to,
                        from_email=from_email).send()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('portfolio:success')
    return render(request, "portfolio/contact.html", {'form': form})

def successView(request):
    return render(request, "portfolio/success.html")
