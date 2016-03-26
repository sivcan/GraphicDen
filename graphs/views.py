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
	#json_data=[]
	i=1
	fieldnames = ("date","data3")
	reader = csv.DictReader(csvfile,fieldnames)
	for row in reader:
		json.dump(row, jsonfile)
		#jsonfile.write(',\n')
		#print ("" + str(row))
		if i != 1:
			json_data.append(row)
		i=i+1

	print(str(json_data))

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
	print(str(json_data))
	return render(request, "khatterd3.html", { "p" : json.dumps(json_data)})
