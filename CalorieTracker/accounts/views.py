# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile  # Correct import for UserProfile
from .forms import UserProfileForm  # Correct import for UserProfileForm


@login_required
def update_profile(request):
    """
    This view allows the user to update their profile.
    It retrieves or creates a UserProfile for the logged-in user
    and displays a form to update it.
    """
    # Get or create the user profile for the logged-in user
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        # Assuming you have a form to handle the profile updates
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')  # Redirect to the profile page or another page
        else:
            messages.error(request, 'There was an error updating your profile.')

    else:
        # If the form is not being submitted, show the current profile data in the form
        form = UserProfileForm(instance=user_profile)

    # Access the username through the user instance
    username = user_profile.user.username

    return render(request, 'accounts/profile.html', {
        'form': form,
        'username': username,
        'user_profile': user_profile,
    })
def register(request):
    """
    This view handles the registration of a new user.
    It uses Django's built-in UserCreationForm.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = UserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})