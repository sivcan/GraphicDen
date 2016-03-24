from django.http import HttpResponse
from django.shortcuts import render,redirect
import datetime
from blog.forms import GraphForm
from blog.models import User


def adder(request):
	if request.method=='POST':
		form=GraphForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('/index/')
	else:
		form=GraphForm()
		return render(request, 'ipform.html', {'form': form })

def index(request):
	return render(request, 'index.html')

def loginportal(request):
	return render(request, 'login.html')
