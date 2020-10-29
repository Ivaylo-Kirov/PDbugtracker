from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('login')
    else:

        form = UserRegisterForm()
    
    context = {
        'form': form,
        'title': 'User Registration'
    }    
    return render(request, 'users/register.html', context)

@login_required
def profile(request):

    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user) # including request.POST as the first parameter passes the updated form values when the form is submitted
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile) #since this includes image file data, you also need the second request.FILES parameter

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Profile updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user) # passing the current user instance allows you to prepopulate the form fields
        p_form = ProfileUpdateForm(instance=request.user.profile)

    

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)