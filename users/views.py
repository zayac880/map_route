from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .forms import UserRegistrationForm


def home(request):
    return render(request, 'home.html')


class UserRegistrationView(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))
        else:
            return render(request, 'register.html', {'form': form})