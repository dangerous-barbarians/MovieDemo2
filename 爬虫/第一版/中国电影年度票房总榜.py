import requests
import re
import random
import time
import pandas as pd


# 获得页面源码
def get_page(url):
	# User_Agent列表
	user_agent_list = [
		"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60",
		"Opera/8.0 (Windows NT 5.1; U; en)",
		"Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50",
		"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50",
		"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
		"Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
		"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
		"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
		"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
		"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16",
		"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36",
		"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
		"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16",
		"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36",
		"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
		"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
		"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
		"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
		"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
		"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
		"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
		"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0",
		"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)",
		"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36",
		"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36",
		"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
		"Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
		"Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
		"Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
		"Mozilla/5.0 (Linux; U; Android 2.2.1; zh-cn; HTC_Wildfire_A3333 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
		"Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
		"MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
		"Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
		"Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
		"Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
		"Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
		"Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
		"Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
		"UCWEB7.0.2.37/28/999",
		"NOKIA5700/ UCWEB7.0.2.37/28/999",
		"Openwave/ UCWEB7.0.2.37/28/999"
	]
	# 产生一个随机User-Agent
	proxy_list = [
		{
			'http': '110.18.2.44:11176',
		},
	]
	proxies = random.choice(proxy_list)
	headers = {
		# 从上面列表中随机取出一个
		'User-Agent': random.choice(user_agent_list)
	}
	# response = requests.get(url, headers=headers, proxies=proxies,)
	response = requests.get(url, headers=headers, )
	# print(proxies)
	if response.status_code == 200:
		return response.text
	else:
		return 'Crawl Failed'


def parse_html_ID(html):
	# 获得电影ID和名称
	pattern = re.compile('<ul.*?hrefTo,href.*?/(\d+).">.*?<p class="first-line">(\w+)</p>.*?"second-line">(\d+).*?</p>',
	                     re.S)
	result = re.findall(pattern, html)
	return result


def parse_html_detial(html):
	# 获得电影日票房,占比，日期
	pattern = re.compile('"box".*?(\d+).*?"onlineBoxRate".*?"(.*?)".*?"showDate".*?(\w+)', re.S)
	result = re.findall(pattern, html)
	# print(result)
	return result


if __name__ == "__main__":
	# 爬取每部电影的ID
	html_id = get_page('http://piaofang.maoyan.com/rankings/year?_v_=yes')
	data_id = parse_html_ID(html_id)
	# print(data)
	for id in data_id:
		# id, name, year
		# print(id)
		year = int(id[2])
		if (year == 2020 or year == 2021):
			detial_url = "http://piaofang.maoyan.com/movie/" + id[0] + "/boxshow?wkwebview=1"
			# print(year)
			print(id)
			# print(detial_url)
			html_detial = get_page(detial_url)
			name = re.findall('<div.*?"info-title-bar">(\w+)</div>', html_detial)
			name = str(name)
			# print(name)
			# 票房，占比，日期
			date_ticket = parse_html_detial(html_detial)
			if len(date_ticket) == 0:
				print("##########数据爬取失败##########")
				break
			##读取数据写入csv
			box_office = []
			percent = []
			date = []
			for item in date_ticket:
				# print(item)
				# print(item[0])
				# print(item[1])
				# print(item[2])
				box_office.append(int(item[0]))
				percent.append(item[1])
				date.append(item[2])
			dataframe = pd.DataFrame({
				'电影名称': name,
				'综合票房': box_office,
				'网售占比': percent,
				'日期': date,
			})
			dataframe.to_csv('data' + name + '.csv', index=False, sep=',', encoding='gbk')
			print('data' + name + '.csv')
			# 随机延时，降低爬取速度
			time.sleep(random.random() * 3)

# 若需要额外的榜单外的电影，可以直接去猫眼查询电影名称，
# 然后查看网页源码，使用ctrl + f 搜索 movieid，就可以知道，电影对应的ID号，
# 直接在下面的代码中修改id，替换上面的主函数部分即可。
if __name__ == "__main__":
	# #爬取每部电影的ID
	# html_id = get_page('http://piaofang.maoyan.com/rankings/year?_v_=yes')
	# data_id = parse_html_ID(html_id)
	# # print(data)
	# for id in data_id:
	#     #id, name, year
	#     print(id)
	#     year = int(id[2])
	#     if(year == 2020 or year == 2021):

	# 一点就到家
	id = '1331267'
	# id = '1222234'

	detial_url = "http://piaofang.maoyan.com/movie/" + id + "/boxshow?wkwebview=1"
	print(id)
	print(detial_url)
	html_detial = get_page(detial_url)
	####获取电影名称
	name = re.findall('<div.*?"info-title-bar">(\w+)</div>', html_detial)
	name = str(name)
	print(name)
	# 票房，占比，日期
	date_ticket = parse_html_detial(html_detial)
	if len(date_ticket) == 0:
		print("##########数据爬取失败##########")
	##读取数据写入csv
	box_office = []
	percent = []
	date = []
	for item in date_ticket:
		# print(item)
		# print(item[0])
		# print(item[1])
		# print(item[2])
		box_office.append(int(item[0]))
		percent.append(item[1])
		date.append(item[2])
	dataframe = pd.DataFrame({
		'电影名称': name,
		'综合票房': box_office,
		'网售占比': percent,
		'日期': date,
	})
	dataframe.to_csv('data' + name + '.csv', index=False, sep=',', encoding='gbk')
	print('data' + name + '.csv')
	# 连续爬取时，随机延时，降低爬取速度，防止ip被封
	time.sleep(random.random() * 3)
