from urllib.request import urlopen

import http.client

from xml.etree import ElementTree
import urllib

from datetime import datetime
class forecastInfo:
    def __init__(self,nx, ny, base_date, base_time, category, fcstTime, fcstValue):
        self.nx = nx
        self.ny = ny
        self.base_date = base_date
        self.base_time = base_time
        self.category = category
        self.fcstTime= fcstTime
        self.fcstValue = fcstValue


class WeatherForecast:
    #End_Point
    End_Point = 'http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastSpaceData?'
    # 일반 인증키
    key = 'ServiceKey=' + 'sqzrjxFFd5WX3hf5KetFKPC9StDxln3sbsk3V2CzIg2yMKCYAQmrTayFhk78aYuXs2ToJNRSNP%2FweK%2FroyJ%2Fng%3D%3D'
    # 로컬 xml 파일
    filename = "LocalWeather.xml"

    def __init__(self, nx, ny):
        self.nx = 'nx=' + str(nx)
        self.ny = 'ny=' + str(ny)
        self.base_date = 'base_date='
        self.base_time = 'base_time='
        pass

    def call_weather(self):
        #return값은 현재시각중 최신 기상예보를 리스트화해서 넘긴다.
        # timedata 만들어야됨
        ##
        now = datetime.now()

        if int(now.day) < 10:
            day = '0' + str(now.day)
        else:
            day = str(now.day)

        if int(now.month) < 10:
            month = '0' + str(now.month)
        else:
            month = str(now.month)

        if int(now.hour) < 10:
            hour = '0' + str(now.hour)
        else:
            hour = str(now.hour)

        if int(now.minute) < 10:
            minute = '0' + str(now.hour)
        else:
            minute = str(now.hour)

        self.base_date += str(now.year) + month + day
        self.base_time += hour + minute

        url = self.End_Point \
              + self.key + '&' \
              + self.base_date + '&' \
              + self.base_time + '&' \
              + self.nx + '&' \
              + self.ny
        #req = urllib.request.Request(url)
        response = urllib.request.urlopen(url)
        data = response.read()

        f = open(WeatherForecast.filename, "wb")
        f.write(data)
        f.close()

        targetXML = open(WeatherForecast.filename)
        tree = ElementTree.parse(targetXML)
        root = tree.getroot()
        items = root.find('body')
        items = items.find('items')

        infolist = []
        for element in items.findall("item"):
            category = element.find('category').text
            fcstTime = element.find("fcstTime").text
            fcstValue = element.find("fcstValue").text
            fcst = forecastInfo(self.nx, self.ny, self.base_date, self.base_time,
                                         category, fcstTime, fcstValue )
            infolist.append(fcst)

            print(fcst.base_date)
            print(fcst.base_time)
            print(fcst.category)
            print(fcst.fcstValue)
            print(fcst.fcstTime)
            print(fcst.nx)
            print(fcst.ny)
            print('')
        targetXML.close()
        return infolist

WeatherForecast(55,127).call_weather()