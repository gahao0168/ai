from django.db import models
from django.utils import timezone
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField

class Post(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	pub_date = models.DateTimeField(default=timezone.now)
	class Meta:
		ordering = ('-pub_date',)
	def __str__(self):
		return self.title

class Country(models.Model):
	country_id = models.IntegerField()
	name = models.CharField(max_length=50)
	def __str__(self):
		return self.name

class City(models.Model):
	name = models.CharField(max_length=50)
	country = models.ForeignKey(Country, on_delete=models.CASCADE)
	population = models.IntegerField()
	def __str__(self):
		return self.name

class Note(models.Model):
	title = models.CharField(max_length=200)
	pub_date = models.DateTimeField(default=timezone.now)
	def __str__(self):
		return self.title

class Func(models.Model):
    name = models.CharField(max_length=100)    # 功能名稱
    content = models.TextField()			   # 功能內容

# 寵寵欲動的功能
class TTYDFunc(models.Model):
    name = models.CharField(max_length=100)    # 功能名稱
    content = models.TextField()			   # 功能內容
    feed_time = models.JSONField()