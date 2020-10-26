from django.shortcuts import render

items = [
    {'desc': 'Main Admin - Users - seems like a perfect setup for Django'},
    {'desc': 'Projects with associated users - Model'},
    {'desc': 'Bugs are associated with Projects - Model'},
    {'desc': 'Bugs have description and attachments - Model'},
    {'desc': 'Email deployments'},
    {'desc': 'Screens:'},
    {'desc': 'Login/Auth'},
    {'desc': 'Profile'},
    {'desc': 'Projects List'},
    {'desc': 'Bugs List'},
    {'desc': 'Bug Detail'},
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