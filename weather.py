from urllib.request import urlopen

import http.client
import copy
from xml.etree import ElementTree
import urllib

from datetime import datetime

time_table = ["0200", "0500", "0800", "1100", "1400", "1700", "2000", "2300"]
category_table = { "POP" : "강수확률",
                   "PTY" : "강수형태",
                   "R06" : "6시간 강수량",
                   "S06" : "6시간 신적설",
                   "REH" : "습도",
                   "SKY" : "하늘상태",
                   "T3H" : "3시간 기온",
                   "TMN" : "아침 최저기온",
                   "TMX" : "낮 최고기온",
                   "UUU" : "풍속(동서성분)",
                   "VVV" : "풍속(남북성분)",
                   "WAV" : "파고",
                   "VEC" : "풍향",
                   "WSD" : "풍속"
                   }

class forecastInfo:
    def __init__(self,nx, ny, base_date, base_time, category, fcstDate, fcstTime, fcstValue):
        self.nx = nx
        self.ny = ny
        self.base_date = base_date
        self.base_time = base_time

        self.category = category_table[category]

        self.fcstDate = fcstDate
        self.fcstTime= fcstTime
        self.fcstValue = fcstValue

        self.valuelist = []
    def print(self):
        if len(self.valuelist) != 0:
            for element in self.valuelist:
                print(element[0])

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
            minute = '0' + str(now.minute)
        else:
            minute = str(now.minute)

        self.base_date += str(now.year) + month + day
        self.base_time += base_time_comp(hour + minute)
        #self.base_date += "20190529"
        #self.base_time += "0200"
        url = self.End_Point \
              + self.key + '&' \
              + self.base_date + '&' \
              + self.base_time + '&' \
              + self.nx + '&' \
              + self.ny + '&' \
              + 'numOfRows=' + str(len(category_table) * 8)
        # Category Table의 길이 = 한 시간에 대한 최대 예보수. 따라서 3시간간격 * 8 = 24시간, 지금시간으로부터 1일동안의 예보를 받아온다.

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
        print(url)
        for element in items.findall("item"):

            base_date = element.find('baseDate').text
            base_time = element.find('baseTime').text
            category = element.find('category').text
            fcstDate = element.find('fcstDate').text
            fcstTime = element.find("fcstTime").text
            fcstValue = element.find("fcstValue").text
            fcst = forecastInfo(self.nx, self.ny, base_date, base_time,
                                         category, fcstDate, fcstTime, fcstValue )
            infolist.append(fcst)

            fcst.print()
            print('')
        targetXML.close()

        # infolist에 전부 들어있다.

        index = 0
        finallist = []
        for i in range(8):
            fcst = copy.deepcopy(infolist[index])
            while fcst.fcstDate == infolist[index].fcstDate and \
                fcst.fcstTime == infolist[index].fcstTime:
                dataset = (infolist[index].category,infolist[index].fcstValue)
                fcst.valuelist.append(dataset)
                index += 1
            finallist.append(fcst)


        return finallist

def base_time_comp(base_time):

    time = int(base_time)
    for i in range(7, 0, -1):
        if  time < int(time_table[i]) + 10:
            base_time = time_table[i-1]


    return base_time

WeatherForecast(55,127).call_weather()
