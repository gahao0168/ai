import os
import django
import pandas as pd
import time
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'datacenter.settings')
django.setup()

from mysite.models import Country, City
url = "https://simpleisbetterthancomplex.com/tutorial/2020/01/19/how-to-use-chart-js-with-django.html"
raw_data = pd.read_html(url)
time.sleep(3)

data = raw_data[0]
data_c = raw_data[1]
# data_c['countries']['id'] 在country裡面的id位置
# data['cities']['country_id'] 在city裡面id的位置
cities = list()
for i in range(len(data)):
	temp = tuple(data['cities'].iloc[i])
	cities.append(temp)

country_dic = dict() 
country_dic['id'] = data_c['countries']['id']
country_dic['name'] = data_c['countries']['name']
for city in cities:
	for country_id in data_c['countries']['id']:
		if city[2] == country_id:
			country_name = country_dic['name'][country_id-1]
			temp = City(name=city[1], country=Country.objects.get(name=country_name), population=city[3])
			temp.save()
			break

# for city in cities:
# 	country = Country.objects.get(country_id=city[2])
# 	temp = City(name=city[1], country=country, population=city[3])
# 	temp.save()


cities = City.objects.all()
print("Done!")