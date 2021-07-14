from django.shortcuts import render, redirect
from django.http import HttpResponse
import random
from mysite.models import Post, Country, City

# Create your views here.
def index(request):
	names = "謝昌儒"
	lotto = [random.randint(1,49) for i in range(6)]
	special = lotto[0]
	lotto = lotto[1:6]
	return render(request, "index.html", locals())

def news(request):
	posts = Post.objects.all()
	return render(request, "news.html", locals())

def show(request, id):
	try:
		post = Post.objects.get(id=id)
	except:
		return redirect("/news/")
	return render(request, "show.html", locals())

def rank(request):
	if request.method == 'POST':
		id = request.POST['id']
		try:
			country = Country.objects.get(id=id)
			cities = City.objects.filter(country=country).order_by('-population')
		except:
			redirect("/rank/")
			cities = City.objects.all().order_by('-population')
	else:
		cities = City.objects.all().order_by('-population')
	countries = Country.objects.all()
	return render(request, "rank.html", locals())