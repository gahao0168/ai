from django.shortcuts import render
from django.http import HttpResponse
import random
from mysite.models import Post

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

def show(request):
	return render(request, "show.html", locals())