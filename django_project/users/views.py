from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


# Create your views here.
def register(request):
    # Validate the form data with this conditional
    if request.method == 'POST':  
        form = UserRegisterForm(request.POST)
        if form.is_valid():  #Back end django code to perform all the checks on user input. Username, password, strength
            form.save()     # Will hash the password and save to database. 
            username = form.cleaned_data.get('username')  # grabbing the username from the form. 
            messages.success(request, f'Your account has been created! You are now able to log in!') # Confirmation of user created. Need to add message to base.html view https://docs.djangoproject.com/en/4.2/ref/settings/#std-setting-MESSAGE_TAGS
            return redirect('login') # then redirect user to the home page. 
    else:
        form = UserRegisterForm()
    return render(request, template_name='users/register.html', context={'form': form})


@login_required  # Decorator to be added. Needs to be imported. Adds login security. 
def profile(request):
    if request.method == 'POST':  
        u_form = UserUpdateForm(request.POST, 
                                instance=request.user)
        p_form = ProfileUpdateForm(request.POST, 
                                   request.FILES, 
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!') 
            return redirect('profile')
    else: 
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)

