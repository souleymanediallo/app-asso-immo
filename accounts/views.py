from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm


# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Votre compte a bien été créé {username}")
            return redirect('home')
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, "accounts/register.html", context)


@login_required
def dashboard(request):
    return render(request, "accounts/dashboard.html")