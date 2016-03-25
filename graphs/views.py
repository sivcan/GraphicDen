from django.http import HttpResponse
from django.shortcuts import render,redirect
import datetime

from blog.forms import GraphForm
from blog.models import User

import csv
import json

import os


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

def grapher(request):
	a=User.objects.all()
	p=a[7]
	return render(request, 'graph.html', locals())

def converter(request):
	a=User.objects.all()
	p=str(a[10])
	csvfile = open(p, 'r')
	jsonfile = open('djangojson.json', 'w')

	fieldnames = ("date","value")
	reader = csv.DictReader(csvfile,fieldnames)
	for row in reader:
	    json.dump(row, jsonfile)
	    jsonfile.write('\n')

	return redirect('/index/')
