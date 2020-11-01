from django.shortcuts import render

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