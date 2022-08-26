from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from .models import PatientRequest, Patient, Provider, Scheduler
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.

# @login_required
 
def Home(request):
    #return render(request, '../provider/templates/home.html')
    return render(request, 'home.html')


def Schedule(request):
    return render(request, 'schedule.html')

def Client_list(request):
    return render(request, 'client.html')



class Signup(View):
#for a patient to sign-up for patient portal
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)

