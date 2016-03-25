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
			return redirect('/convert/')
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
	p='static/media/'
	jsonfilewr='static/media/files/'
	p+=str(a[12])
	csvfile = open(p, 'r')
	jsonfilewr+='djangojson.json'
	jsonfile = open(jsonfilewr, 'w')

	fieldnames = ("date","value")
	reader = csv.DictReader(csvfile,fieldnames)
	for row in reader:
		json.dump(row, jsonfile)
		jsonfile.write('\n')
		
	return redirect ('/hardcode/')
	#return render(request, 'graph.html', {"p":jsonfilewr})


def hardcode(request):
	p="[{ key: 0, value: 5 },{ key: 1, value: 10 },{ key: 2, value: 13 },{ key: 3, value: 19 },{ key: 4, value: 21 },{ key: 5, value: 25 },{ key: 6, value: 22 },{ key: 7, value: 18 },{ key: 8, value: 15 },{ key: 9, value: 13 },{ key: 10, value: 11 },{ key: 11, value: 12 },{ key: 12, value: 15 },{ key: 13, value: 20 },{ key: 14, value: 18 },{ key: 15, value: 17 },{ key: 16, value: 16 },{ key: 17, value: 18 },{ key: 18, value: 23 },{ key: 19, value: 29 } ];"
	return render(request, 'sampled3.html', locals())
