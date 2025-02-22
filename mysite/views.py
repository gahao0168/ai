from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from mysite.models import Post, Country, City, Func, TTYDFunc, FeedTime
from mysite.forms import RegisterForm, LoginForm, FunctionForm, TTYDFunctionForm
# from django.contrib import messages


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

# 註冊
def sign_up(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():	
        	form.save()
        	# messages.success(request, 'Account created successfully')

        	username = request.POST.get("username")
	        data = FeedTime()
	        user = FeedTime.objects.filter(username=username)
	        selected = user
	        data.username = username
	        data.save()

	        username = form.cleaned_data.get('username')
	        raw_password = form.cleaned_data.get('password1')
	        user = authenticate(username=username, password=raw_password)
	        login(request, user)  # 直接登入
        	return redirect("/")  # 並重新導向到首頁

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

def mylogout(request):
	logout(request)
	return redirect("/login/")

def updateF(request, pk):
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
   	return render(request, "updateF.html", context)

def deleteF(request, pk):
   	function = Func.objects.get(id=pk)

   	if request.method == "POST":
   		function.delete()
   		return redirect('/')

   	context = {
   		'function':function
   	}
   	return render(request, "deleteF.html", context)

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

def deleteTF(request, pk):
   	ttydfunction = TTYDFunc.objects.get(id=pk)

   	if request.method == "POST":
   		ttydfunction.delete()
   		return redirect('/about/')

   	context = {
   		'function':ttydfunction
   	}
   	return render(request, "deleteTF.html", context)

def updateTF(request, pk):
   	ttydfunction = TTYDFunc.objects.get(id=pk)

   	form = TTYDFunctionForm(instance=ttydfunction)

   	if request.method == "POST":
   		form = TTYDFunctionForm(request.POST, instance=ttydfunction)
   		if form.is_valid():
   			form.save()
   		return redirect("/about/")
   	context = {
   		'form':form
   	}
   	return render(request, "updateTF.html", context)

def set(request):
	username = request.user.username
	data = FeedTime()
	user = FeedTime.objects.filter(username=username)
	times = range(24)
	selected = user
	if request.method == "POST":
		if request.POST.getlist('time') is not None:
			selected = request.POST.getlist('time')

			data.username = request.user.username
			try:
				data.feed_time1 = selected[0]
				data.feed_time2 = selected[1]
				data.feed_time3 = selected[2]
			except:
				pass

			try:
				# 存進資料庫前，先刪除該使用者以前的紀錄
				user.delete() # 刪除上一筆
				data.save()   # 記錄這一筆
			except:
				pass

			return render(request, "set.html", locals())
		else:
			selected = list()

	return render(request, "set.html", locals())