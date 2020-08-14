from django.shortcuts import render, redirect
from .forms import (UserRegisterForm,
                    UserUpdateForm, ProfileUpdateForm)

from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('username')
            form.save()
            messages.success(request, f'Account for {user} created')
            return redirect('posts-home')
    else:
        form = UserRegisterForm()
    template_name = "users/register.html"
    context = {'form': form}
    return render(request, template_name, context)


@login_required
def profile(request):
    template_name = "users/profile.html"
    u_form = UserUpdateForm(request.POST, instance=request.user)
    p_form = ProfileUpdateForm(
        request.POST, request.FILES, instance=request.user.profile)
    if u_form.is_valid() and p_form.is_valid():
        u_form.save()
        p_form.save()
        messages.success(request, f'Your account has been updated')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {'p_form': p_form, 'u_form': u_form}
    return render(request, template_name, context)
