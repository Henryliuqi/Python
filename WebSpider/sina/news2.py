import requests
from bs4 import BeautifulSoup
from datetime import datetime

res = requests.get('http://news.sina.com.cn/c/nd/2018-03-10/doc-ifxpwyhw6832680.shtml')
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text, 'html.parser')

title = soup.select('.main-title')[0].text
time = soup.select('.date')[0].text
source = soup.select('.source')[0].text
print(source,time,title)
ta = datetime.strptime(time, '%Y年%m月%d日 %H:%M')
print(time)
print(ta)