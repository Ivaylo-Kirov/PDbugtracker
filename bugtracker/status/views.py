from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import ContactForm
from django.contrib import messages


items = [
    {'desc': 'Bugs have description and attachments - Model'},
    {'desc': 'Email deployments'},
]

# Create your views here.
def home(request):
    context = {
        'items': items,
        'title': 'Home'
    }
    return render(request, 'status/home.html', context)

def about(request):
    return render(request, 'status/about.html', {'title': 'About'})

class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'status/contact.html'
    success_url = '/'

    def form_valid(self, form):

        # this method gets called when valid data was submitted and it expects an HttpResponse
        form.send_email() # form here represents the ContactForm instance defined in forms.py as a class
        messages.success(self.request, f'Your email has been sent. Thank you.')
        return super().form_valid(form) # return will look for the success_url
