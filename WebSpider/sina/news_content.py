import requests
from bs4 import BeautifulSoup
from datetime import datetime



def getNewsDetail(newsurl):
  result = {}
  article = []
  res = requests.get(newsurl)
  res.encoding = 'utf-8'
  soup = BeautifulSoup(res.text, 'html.parser')

  result['title'] = soup.select('.main-title')[0].text
  result['newssource'] = soup.select('.source')[0].text
  time = soup.select('.date')[0].text
  # result['dt'] = datetime.strptime(time, '%Y年%m月%d日 %H:%M')
  result['dt'] = time

  for p in soup.select('.article p')[:-2]:
    article.append(p.text.strip())
  result['article'] = article
  print(result)

getNewsDetail('http://news.sina.com.cn/c/nd/2018-03-10/doc-ifxpwyhw6832680.shtml')