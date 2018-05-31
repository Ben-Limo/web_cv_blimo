from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail

from django.conf import settings
from .forms import CreateForm, UserDataCreateForm
from .models import UserData
# Create your views here.

class HomePageView(SuccessMessageMixin, CreateView):
	form_class = UserDataCreateForm
	template_name = "website/index.html"
	success_url = "/#contactMe"
	success_message = "Your data was submitted successfully"

	def form_valid(self, form):

		if form.is_valid():
			name 		= form.cleaned_data['name']
			company		= form.cleaned_data['company']
			emailFrom 	= form.cleaned_data['email']
			comment 	= form.cleaned_data['comment']
			subject 	= 'Message from blimo-cv.herokuapp.com'
			data 		= {'name': name, 'company': company, 'emailFrom': emailFrom, 'comment': comment}
			message 	= "{name} from {company} said:- \n {comment} \n\n You can reach them through: {emailFrom}".format(**data)
			
			emailTo		= [settings.EMAIL_HOST_USER]
			send_mail(subject, message, emailFrom, emailTo, fail_silently= False)

			return super(HomePageView, self).form_valid(form)
