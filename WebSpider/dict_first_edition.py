import urllib.request
import urllib.parse
import json

content = input("please enter the content to be translated: ")

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
data = {}
data['i'] = content
data['type'] = 'AUTO'
# data['to'] = 'AUTO'
data['smartresult'] = 'dict'
data['client'] = 'fanyideskweb'
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data['ue'] = 'UTF-8'
data['action'] = 'FY_BY_CLICKBUTTION'
data['typeResult'] = 'false'
data = urllib.parse.urlencode(data).encode("utf-8")
response = urllib.request.urlopen(url, data)
html = response.read()
html = html.decode("utf-8")
target = json.loads(html)
print("translation results: %s" % (target['translateResult'][0][0]['tgt']))
