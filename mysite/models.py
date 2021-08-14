from django.db import models
from django.utils import timezone

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

class FeedTime(models.Model):
	username = models.CharField(max_length=50)
	feed_time1 = models.IntegerField()
	feed_time2 = models.IntegerField(null=True)
	feed_time3 = models.IntegerField(null=True)
	def __str__(self):
		return self.username