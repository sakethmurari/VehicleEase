from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import *
from .models import Register

def register(request):
    f=registerForm()
    if request.method=='POST':
        form=registerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        form=registerForm()
    return render(request,'register.html',{'form':f})