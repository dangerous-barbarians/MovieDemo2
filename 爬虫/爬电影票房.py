# requests ->pip install requests
# BeautifulSoup -> pip install BeautifulSoup4

import requests
from bs4 import BeautifulSoup

# 通过requests请求到电影票房的网页
text = requests.get("https://ys.endata.cn/BoxOffice/Ranking").text

# 使用BeautifulSoup进行解析
main_page = BeautifulSoup(text, "html.parser")  # 后面这个是html解析器

table = main_page.find("table", attrs={"id": "tbContent"})
# find 找的是一个标签
# find all 找一堆标签
trs = table.find_all  # 拿到每一个tr
for tr in trs:
	lst = tr.find_all("td")  # 找到每一个td
	if len(lst) == 0:
