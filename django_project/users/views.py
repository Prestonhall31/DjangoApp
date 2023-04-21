from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


# Create your views here.
def register(request):
    # Validate the form data with this conditional
    if request.method == 'POST':  
        form = UserRegisterForm(request.POST)
        if form.is_valid():  #Back end django code to perform all the checks on user input. Username, password, strength
            form.save()     # Will hash the password and save to database. 
            username = form.cleaned_data.get('username')  # grabbing the username from the form. 
            messages.success(request, f'Account created for {username}!') # Confirmation of user created. Need to add message to base.html view
            return redirect('blog-home') # then redirect user to the home page. 
    else:
        form = UserRegisterForm()
    return render (request, template_name='users/register.html', context={'form': form})




# Different message types
    # message.debug
    # message.info
    # message.success
    # message.warning
    # message.error