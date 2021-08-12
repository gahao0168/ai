from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from mysite.models import Post, Country, City, Func
from mysite.forms import RegisterForm, LoginForm, FunctionForm, TTYDFunctionForm

# Create your views here.
def index(request):
	functions = Func.objects.all()

	form = FunctionForm()

	if request.method == "POST":
		form = FunctionForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect("/")

	context = {
		'functions':functions,
		'form':form
	}
	return render(request, "index.html", context)

def news(request):
	posts = Post.objects.all()
	return render(request, "news.html", locals())

def delete(request, id):
	try:
		post = Post.objects.get(id=id)
		post.delete()
	except:
		return redirect("/news/")
	return redirect("/news/")

@login_required(login_url="/login/")
def show(request, id):
	try:
		post = Post.objects.get(id=id)
	except:
		return redirect("/news/")
	return render(request, "show.html", locals())

@login_required(login_url="/login/")
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

@login_required(login_url="/login/")
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

# @login_required(login_url="/login/")
# def set(request):
# 	return render(request, "set.html", locals())

# 註冊
def sign_up(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/login/")  #重新導向到登入畫面
    context = {
        'form': form
    }
    return render(request, "register.html", context)

# 登入
def sign_in(request):
    form = LoginForm()
    if request.method == "POST":
	    username = request.POST.get("username")
	    password = request.POST.get("password")
	    user = authenticate(request, username=username, password=password)
	    if user is not None:
	        login(request, user)
	        return redirect('/')  #重新導向到首頁
    context = {
        'form': form
    }
    return render(request, "login.html", context)

def update(request, pk):
   	function = Func.objects.get(id=pk)

   	form = FunctionForm(instance=function)

   	if request.method == "POST":
   		form = FunctionForm(request.POST, instance=function)
   		if form.is_valid():
   			form.save()
   		return redirect("/")
   	context = {
   		'form':form
   	}
   	return render(request, "update.html", context)

def deleteF(request, pk):
   	function = Func.objects.get(id=pk)

   	if request.method == "POST":
   		function.delete()
   		return redirect('/')

   	context = {
   		'function':function
   	}
   	return render(request, "deleteF.html", context)

def mylogout(request):
	logout(request)
	return redirect("/login/")

def about(request):
	ttydfunctions = TTYDFunc.objects.all()

	form = TTYDFunctionForm()

	if request.method == "POST":
		form = TTYDFunctionForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect("/about/")

	context = {
		'functions':ttydfunctions,
		'form':form
	}
	return render(request, "about.html", context)