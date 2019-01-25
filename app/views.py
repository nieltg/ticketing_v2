from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy

@login_required(login_url=reverse_lazy('admin:login'))
def home(request):
    return render(request, "index.html")
