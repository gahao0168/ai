from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import logout
import random
from mysite.models import Post, Country, City
from plotly.offline import plot
import plotly.graph_objs as go
import numpy as np

# Create your views here.
def index(request):
	names = "謝昌儒"
	lotto = [random.randint(1,49) for i in range(6)]
	special = lotto[0]
	lotto = lotto[1:6]
	x = np.linspace(0, 2*np.pi, 360)
	y1 = np.sin(x)
	y2 = np.cos(x)
	plot_div = plot([
		go.Scatter(x=x, y=y1,
			mode='lines', name='SIN',
			opacity=0.8, marker_color='green'),
		go.Scatter(x=x, y=y2,
			mode='lines', name='COS', 
			opacity=0.8, marker_color='blue')
		],output_type='div')
	return render(request, "index.html", locals())

def news(request):
	posts = Post.objects.all()
	return render(request, "news.html", locals())

@login_required(login_url="/admin/login/")
def show(request, id):
	try:
		post = Post.objects.get(id=id)
	except:
		return redirect("/news/")
	return render(request, "show.html", locals())

@login_required(login_url="/admin/login/")
def rank(request):
	if request.method == 'POST':
		id = request.POST['id']
		if id.strip() == 'default':
			return redirect("/rank/")
		try:
			country = Country.objects.get(id=id)
		except:
			return redirect("/rank/")
		cities = City.objects.filter(country=country).order_by('-population')
	else:
		cities = City.objects.all().order_by('-population')
	countries = Country.objects.all()
	return render(request, "rank.html", locals())

@login_required(login_url="/admin/login/")
def chart(request):
	if request.method == 'POST':
		id = request.POST['id']
		if id.strip() == 'default':
			return redirect("/rank/")
		try:
			country = Country.objects.get(id=id)
		except:
			return redirect("/chart/")
		cities = City.objects.filter(country=country).order_by('-population')
	else:
		cities = City.objects.all().order_by('-population')
	countries = Country.objects.all()
	names = [city.name for city in cities]
	population = [city.population for city in cities]
	return render(request, "chart.html", locals())

def mylogout(request):
	logout(request)
	return redirect("/")

def delete(request, id):
	try:
		post = Post.objects.get(id=id)
		post.delete()
	except:
		return redirect("/news/")
	return redirect("/news/")