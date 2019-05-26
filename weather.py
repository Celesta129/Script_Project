from urllib.request import urlopen
#import urllib.request

import http.client

import urllib
from xml.etree import ElementTree

# 일반 인증키
key = 'ServiceKey=' + 'sqzrjxFFd5WX3hf5KetFKPC9StDxln3sbsk3V2CzIg2yMKCYAQmrTayFhk78aYuXs2ToJNRSNP%2FweK%2FroyJ%2Fng%3D%3D'
# End Point : Request는 이쪽으로
EndPoint = 'http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2'
base_date = 'base_date=' + '20190526'
base_time = 'base_time=' + '2000'
nx = 'nx=' + '55'
ny = 'ny=' + '127'

#메세지명 http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastSpaceData
url = 'http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastSpaceData?' \
      + key + '&'\
      + base_date + '&'\
      + base_time + '&'\
      + nx + '&' \
      + ny

req = urllib.request.Request(url)
response = urlopen(url)
data = response.read()

print(url)
filename = "LocalWeather.xml"

f = open(filename,"wb")
f.write(data)
f.close()

targetXML = open(filename)
tree = ElementTree.parse(targetXML)
root = tree.getroot()

items = root.find('body')
items = items.find('items')
#for item in bookElements:
#      strTitle = item.find("title")  # ’title’ 엘리먼트 추출
#     if (strTitle.text.find(keyword) >= 0):  # keyword 검색

for element in root.findall("item"):
     print(element.find("fcstTime"))
     print(element.find("fcstValue"))

targetXML.close()
