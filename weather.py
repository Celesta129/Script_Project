from urllib.request import urlopen

import http.client

from xml.etree import ElementTree
import urllib

# 일반 인증키
key = 'ServiceKey=' + 'sqzrjxFFd5WX3hf5KetFKPC9StDxln3sbsk3V2CzIg2yMKCYAQmrTayFhk78aYuXs2ToJNRSNP%2FweK%2FroyJ%2Fng%3D%3D'
# End Point : Request는 이쪽으로
#EndPoint = 'http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2'
base_date = 'base_date=' + '20190527'
base_time = 'base_time=' + '0200'
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
response = urllib.request.urlopen(url)
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

for element in items.findall("item"):
     print('카테고리 : ' + element.find('category').text)
     print('예보시간 : ' + element.find("fcstTime").text)
     print('예보값 : '+ element.find("fcstValue").text)
     print(' ')

targetXML.close()
