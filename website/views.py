from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from .forms import CreateForm, UserDataCreateForm
from .models import UserData
# Create your views here.

class HomePageView(CreateView):
	form_class = UserDataCreateForm
	template_name = "website/index.html"
	success_url = "/#contactMe"
	# success_message = "You data was submitted successfully."

    #     return render(request, 'index.html', context=None)

# Create your views here.
class AboutPageView(TemplateView):
	template_name = "about.html"


# def create_formview(request):
# 	form = CreateForm(request.POST or None)
# 	errors = None
# 	if form.is_valid():
# 		obj = UserData.objects.create(
# 			name = form.cleaned_data.get('name'),
# 			company = form.cleaned_data.get('company'),
# 			email= form.cleaned_data.get('email'),
# 			comment = form.cleaned_data.get('email')
# 			)
# 		return HttpResponseRedirect("/")
# 	if form.errors:
# 		errors = form.errors

# 	template_name =  "website/index.html"
# 	context = {"form": form, "errors": errors}
# 	return render (request, template_name, context)

