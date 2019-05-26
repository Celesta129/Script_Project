from urllib.request import urlopen
from urllib.parse import urlparse

import http.client
import urllib.request

import urllib
# 일반 인증키
key = 'ServiceKey=' + 'sqzrjxFFd5WX3hf5KetFKPC9StDxln3sbsk3V2CzIg2yMKCYAQmrTayFhk78aYuXs2ToJNRSNP%2FweK%2FroyJ%2Fng%3D%3D'
# End Point : Request는 이쪽으로
EndPoint = 'http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2'
base_date = 'base_date=' + '20190526'
base_time = 'base_time=' + '1800'
nx = 'nx=' + '55'
ny = 'ny=' + '127'

#메세지명 http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastSpaceData
url = 'http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastSpaceData?' \
      + key + '&'\
      + base_date + '&'\
      + base_time + '&'\
      + nx + '&' \
      + ny

request = urllib.request.Request(url)
response = urllib.request.urlopen(request)

print(url)

