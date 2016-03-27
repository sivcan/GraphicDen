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
	x=row[0]
	y=row[1]
	p+=row[2]
	p=p.replace('\n','')
	jsonfilewr='static/media/files/'
	print("yolo  debugging : " + x + y)

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
	#p="[{ key: 0, data3: 5 },{ key: 1, data3: 10 },{ key: 2, data3: 13 },{ key: 3, data3: 19 },{ key: 4, data3: 21 },{ key: 5, data3: 25 },{ key: 6, data3: 22 },{ key: 7, data3: 18 },{ key: 8, data3: 15 },{ key: 9, data3: 13 },{ key: 10, data3: 11 },{ key: 11, data3: 12 },{ key: 12, data3: 15 },{ key: 13, data3: 20 },{ key: 14, data3: 18 },{ key: 15, data3: 17 },{ key: 16, data3: 16 },{ key: 17, data3: 18 },{ key: 18, data3: 23 },{ key: 19, data3: 29 } ];"
	# p=[{"velocity": "202","time": "2000"},
	# 	{"velocity": "215","time": "2002"},
	# 	{"velocity": "179","time": "2004"},
	# 	{"velocity": "199","time": "2006"}]
	# p=[{
	# 	"velocity": "202",
	# 	"time": "2000"
	# }, {
	# 	"velocity": "215",
	# 	"time": "2002"
	# }, {
	# 	"velocity": "179",
	# 	"time": "2004"
	# }, {
	# 	"velocity": "199",
	# 	"time": "2006"
	# }, {
	# 	"velocity": "134",
	# 	"time": "2008"
	# }, {
	# 	"velocity": "176",
	# 	"time": "2010"
	# }]
	# p=[{"date": "41", "data3": "153"},
	# 	{"date": "42", "data3": "165"},
	# 	{"date": "43", "data3": "269"},
	# 	{"date": "44", "data3": "344"},
	# 	{"date": "45", "data3": "376"},
	# 	{"date": "56", "data3": "410"},
	# 	{"date": "57", "data3": "421"},
	# 	{"date": "68", "data3": "405"},
	# 	{"date": "79", "data3": "376"},
	# 	{"date": "80", "data3": "359"},
	# 	{"date": "91", "data3": "392"},
	# 	{"date": "112", "data3": "433"},
	# 	{"date": "113", "data3": "455"},
	# 	{"date": "114", "data3": "478"}]
	domain_x_min=99999
	domain_x_max=0
	domain_y_min=99999
	domain_y_max=0
	x_axis=x
	y_axis=y
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


	p=json.dumps(json_data)
	return render(request, "khatterd3.html", locals())#({"p" : json.dumps(json_data), "x" : x, "y" : y,}))# "x" : x, "y" : y})
	
