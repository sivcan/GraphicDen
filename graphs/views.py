
from django.shortcuts import render,redirect
import datetime
from blog.forms import GraphForm


def adder(request):
	if request.method=='POST':
		form=GraphForm(request.POST)
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
