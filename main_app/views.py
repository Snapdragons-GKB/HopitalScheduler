
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

#@method_decorator(login_required, name='dispatch')
def Home(request):
    #return render(request, '../main_app/templates/home.html')
    return render(request, 'home.html')


def About(request):
    return render(request, 'about.html')

def Patient_Request(request):
    return render(request, 'about.html')

def Patient_Details(request):
    # patient = Patient.Patient_id.objects.all()
    return render(request, 'details.html')

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
            return redirect("home")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)

