import os
import requests  # 发送HTTP请求
import random  #
import time
from bs4 import BeautifulSoup
from lxml import etree
import threading
from fake_useragent import UserAgent
import pandas as pd
import numpy as np  # 用于计算
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.charts import Bar
from pyecharts.charts import Pie
from pyecharts.charts import Line
from pyecharts.charts import Funnel
from pyecharts.faker import Faker

ua = UserAgent(use_cache_server=False)
headers = {
	'User-Agent': ua.chrome,
}
url = 'https://movie.douban.com/top250?start=0&filter='
request = requests.get(url, headers=headers)
print(request)

BsBOJ = BeautifulSoup(request.content, 'lxml')
pic = BsBOJ.find_all(attrs={'class': 'pic'})
film_urls = []
for x in pic:
	href = x.a.get('href')
	film_urls.append(href)
print(film_urls)

for i in range(len(film_urls)):
	href = film_urls[i]
	# print(href)
	time.sleep(random.randint(2, 7))
	r = requests.get(href, headers=headers, timeout=10)
	r.encoding = 'utf-8'
	BsBOJ = BeautifulSoup(r.text, 'html.parser')
	# 排名
	rank = BsBOJ.find(attrs={'class': 'top250-no'}).text.split('.')[1]
	# 电影名
	film_name = BsBOJ.find(attrs={'property': 'v:itemreviewed'}).text.split(' ')[0]  # split 将中英文从空格处分开
	# 导演
	director = BsBOJ.find(attrs={'id': 'info'}).text.split('\n')[1].split(':')[1].split('/')
	# 编剧
	scriptwriter = BsBOJ.find(attrs={'id': 'info'}).text.split('\n')[2].split(':')[1].split('/')
	# 主演
	actor = BsBOJ.find(attrs={'id': 'info'}).text.split('\n')[3].split(':')[1].split('/')
	# 类型
	filmtype = BsBOJ.find(attrs={'id': 'info'}).text.split('\n')[4].split(':')[1].split('/')  #
	if BsBOJ.find(attrs={'id': 'info'}).text.split('\n')[5].split(':')[0] == '官方网站':
		# 制片国家/地区
		area = BsBOJ.find(attrs={'id': 'info'}).text.split('\n')[6].split(':')[1].split('/')  #
		# 语言
		language = BsBOJ.find(attrs={'id': 'info'}).text.split('\n')[7].split(':')[1].split('/')  #
		# 上映日期
		initialReleaseDate = \
			min(BsBOJ.find(attrs={'id': 'info'}).text.split('\n')[8].split(':')[1].split('/')).split('(')[0]  #
	else:

		# 制片国家/地区
		area = BsBOJ.find(attrs={'id': 'info'}).text.split('\n')[5].split(':')[1].split('/')  #
		# 语言
		language = BsBOJ.find(attrs={'id': 'info'}).text.split('\n')[6].split(':')[1].split('/')  #
		# 上映日期
		initialReleaseDate = \
			min(BsBOJ.find(attrs={'id': 'info'}).text.split('\n')[7].split(':')[1].split('/')).split('(')[0]  #
	# 片长
	runtime = BsBOJ.find(attrs={'property': 'v:runtime'}).text  #
	# 评分（平均分）
	rating_num = BsBOJ.find(attrs={'property': 'v:average'}).text  #
	# 五星百分比
	stars5_rating_per = BsBOJ.find(attrs={'class': 'rating_per'}).text  #
	# 评价人数
	rating_people = BsBOJ.find(attrs={'property': 'v:votes'}).text  #
	film_info = [rank, film_name, director, scriptwriter, actor, filmtype, area, language, initialReleaseDate, runtime,
	             rating_num, stars5_rating_per, rating_people]
	print(film_info)
	head = ['rank', 'film_name', 'director', 'scriptwriter', 'actor', 'filmtype', 'area', 'language',
	        'initialReleaseDate', 'runtime', 'rating_num', 'stars5_rating_per', 'rating_people']
	# df2.to_csv('douban_top250_test.csv', mode='a', header=head, index=None)
	current_path = os.path.dirname('__file__')
	if film_info[0] == '1':
		df2.to_csv(current_path + 'douban_top250_test.csv', mode='a', header=head, index=None)
		print(f"top{film_info[0]}爬取完成")
	else:
		df2.to_csv(current_path + 'douban_top250_test.csv', mode='a', header=False, index=None)
		print(f"top{film_info[0]}爬取完成")
