from __future__ import unicode_literals
from .models import Temperature 
from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
def index(request):
	t = Temperature.objects.all()[len(Temperature.objects.all()) - 1]
	t = str(t)
	t = t.split(',')
	te = str(int(str(t[0])))
	hum = str(int(str(t[1])))
	sm =  str(int(str(t[2])))
	lvl =  str(int(str(t[3])))
	date = str(t[4])
	context = {'t': te, 'h': hum,'sm':sm,'lvl':lvl,'d': date}
	return render(request,'temperature/index.html',context)
def getdata(request):
	if request.method=='GET' :
		temp_value=request.GET['temperature']
		hum_value = request.GET['humidity']
		time = request.GET['time']
		sm = request.GET['soil']
		lvl = request.GET['water']
		t_obj=Temperature()
		t_obj.tem_value=temp_value
		t_obj.hum_value = hum_value
		t_obj.soil_mois = sm
		t_obj.wat_lvl = lvl
		t_obj.time=time
		t_obj.save()
		return HttpResponse("data saved in db")
	else:
		return HttpResponse("error")
def html(request):
	temp1=[]
	hum=[]
	t = Temperature.objects.all()[len(Temperature.objects.all()) - 1]
	t = str(t)
	t = t.split(',')
	te = str(int(str(t[0])))
	hu = str(int(str(t[1])))
	sm =  str(int(str(t[2])))
	lvl =  str(int(str(t[3])))
	date = str(t[4])
	for i in range(1,11):
		temp = Temperature.objects.all()[len(Temperature.objects.all()) - i]
		temp = str(temp)
		temp = temp.split(',')
		temp1.append(int(temp[0]))
		hum.append(int(temp[1]))
	context = {'t': te, 'h': hu,'sm':sm,'lvl':lvl,'d': date,'tem':temp1,'hum':hum}
	return render(request,'temperature/1.html',context)
def html1(request):
	t = Temperature.objects.all()[len(Temperature.objects.all()) - 1]
	t = str(t)
	t = t.split(',')
	te = str(int(str(t[0])))
	hu = str(int(str(t[1])))
	lvl =  str(int(str(t[3])))
	date = str(t[4])
	sm = Temperature.objects.all()[len(Temperature.objects.all()) - 1]
	sm = str(sm)
	sm = sm.split(',')
	sm = int(sm[2])
	context = {'t': te, 'h': hu,'sm':sm,'lvl':lvl,'d': date}
	return render(request,'temperature/001.html',context)
def html2(request):
	return render(request,'temperature/002.html')
