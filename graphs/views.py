from django.http import HttpResponse
from django.shortcuts import render,redirect
import datetime
from django.utils.safestring import mark_safe
from blog.forms import GraphForm
from blog.models import User

import csv
import json

import os

json_data=[]

def clear():
	del json_data[:]


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


def converter(request):
	a=User.objects.all()
	row = a[len(a)-1]
	row=str(row)
	p='static/media/'
	row=row.split(",")
	global x
	global y
	global type_graph
	x=row[0]
	y=row[1]
	p+=row[2]
	type_graph=row[3]
	p=p.replace('\n','')
	jsonfilewr='static/media/files/'
	print("yolo  debugging : " + x + y +" " + type_graph)

	csvfile = open(p, 'r')
	jsonfilewr+='djangojson.json'
	jsonfile = open(jsonfilewr, 'w')
	#json_data=[]
	i=1
	fieldnames = (x,y)
	reader = csv.DictReader(csvfile,fieldnames)
	for row in reader:
		#json.dump(row, jsonfile)
		#jsonfile.write(',\n')
		#print ("" + str(row))
		if i != 1:
			json_data.append(row)
		i=i+1


	return redirect ('/success/')
	#return render(request, 'graph.html', {"p":jsonfilewr})


def hardcode(request):
	domain_x_min=99999999999
	domain_x_max=0
	domain_y_min=99999999999
	domain_y_max=0
	x_axis=x
	y_axis=y
	name_x=x_axis
	name_y=y_axis

	#Code to find the minimum and maximum domain ranges.
	for i  in range(0,len(json_data)):
	    domain_x_max=max(domain_x_max,int(json_data[i][str(x_axis)]))

	for i  in range(0,len(json_data)):
	    domain_y_max=max(domain_y_max,int(json_data[i][str(y_axis)]))

	for i in range(0,len(json_data)):
		if int(json_data[i][str(x_axis)]) <= domain_x_min :
			domain_x_min=int(json_data[i][str(x_axis)])

	for i in range(0,len(json_data)):
		if int(json_data[i][str(y_axis)]) <= domain_y_min :
			domain_y_min=int(json_data[i][str(y_axis)])

	print (str(type_graph))
	p=json.dumps(json_data)

	clear() #Clears the json_data else the data used to get appended.
	if 'Bar Graph' in type_graph :
		return render(request, "sampled3.html", locals())
	if 'Line Graph' in type_graph :
		return render(request, "khatterd3.html", locals())
	if 'Pie Graph' in type_graph : 
		return render(request, "bard3.html", locals())
