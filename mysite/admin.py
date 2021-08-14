from django.contrib import admin
from mysite.models import Post, Country, City, Note, Func, TTYDFunc, FeedTime

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')
admin.site.register(Post, PostAdmin)

class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'country_id')
admin.site.register(Country, CountryAdmin)

class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'population')
admin.site.register(City, CityAdmin)

class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')
admin.site.register(Note, NoteAdmin)

class FuncAdmin(admin.ModelAdmin):
    list_display = ('name', 'content')
admin.site.register(Func, FuncAdmin)

class TTYDFuncAdmin(admin.ModelAdmin):
    list_display = ('name', 'content')
admin.site.register(TTYDFunc, TTYDFuncAdmin)

class FeedTimeAdmin(admin.ModelAdmin):
    list_display = ('username','feed_time1', 'feed_time2', 'feed_time3')
admin.site.register(FeedTime, FeedTimeAdmin)