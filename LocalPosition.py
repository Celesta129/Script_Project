from xml.etree import ElementTree

class cityInfo:
    def __init__(self, area, gu, dong, x, y):
        self.area = area
        self.gu = gu
        self.dong = dong
        self.x = x
        self.y = y
    pass

class namedlist:
    def __init__(self,text):
        self.text = text
        self.list = []
    pass
class Pos:
    def __init__(self,name,x,y):
        self.name = name
        self.x = x
        self.y = y


class localPosition:
    Positionlist = None
    filename = "LocalPosition.xml"
    AreaList = []
    def __init__(self):
        if(self.Positionlist == None):
            self.Positionlist = []
            targetXML = open(self.filename,'rt', encoding='UTF8')
            tree = ElementTree.parse(targetXML)
            root = tree.getroot()
            for element in root.findall("text"):
                area = element.find("city").text
                gu =  element.find("gu").text
                dong = element.find("dong").text

                if gu == None:
                    gu = " "

                if dong == None:
                    dong = " "

                x = element.find("X").text
                y = element.find("Y").text

                self.Positionlist.append(cityInfo(area,gu,dong,x,y))
                #print(city +" " + gu + " " + dong + ": " + x + "," + y)
                pass
            targetXML.close()


            area = ""
            gu = ""
            for element in self.Positionlist:
                if area != element.area:
                    area = element.area
                    AreaInfo = namedlist(area)
                    self.AreaList.append(AreaInfo)
                if gu != element.gu:
                    gu = element.gu
                    GuInfo = namedlist(gu)
                    AreaInfo.list.append(GuInfo)

                posinfo = Pos(element.dong, element.x, element.y)
                GuInfo.list.append(posinfo)

                pass
            pass
    def call_PosInfo(self):
        for area in self.AreaList:
            for gu in area.list:
                for dong in gu.list:
                    print(area.text + " " + gu.text + " " + dong.name +" " + dong.x + " " +dong.y)
        return self.AreaList
    pass

localPosition().call_PosInfo()