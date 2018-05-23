from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin

from .forms import CreateForm, UserDataCreateForm
from .models import UserData
# Create your views here.

class HomePageView(SuccessMessageMixin, CreateView):
	form_class = UserDataCreateForm
	template_name = "website/index.html"
	success_url = "/#contactMe"
	success_message = "Your data was submitted successfully"


