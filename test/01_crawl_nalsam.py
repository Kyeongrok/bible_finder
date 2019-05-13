from libs.crawler import crawl
from bs4 import BeautifulSoup
import libs.bibleFinder as finder

url = "http://www.365qt.com/TodaysQT.asp?QTID=7586"
pageString = crawl(url)

def parse(pageString):
    result = {}
    bsObj = BeautifulSoup(pageString, "html.parser")
    # print(bsObj)

    qtDayText2 = bsObj.find("div", {"id":"qtDay"})
    result['qtDayText2'] = qtDayText2.text

    box2Content = bsObj.find("div", {"class":"box2Content"})
    result['box2Content'] = box2Content.text

    script = bsObj.find("div", {"class":"script"})
    result['srcipt'] = script.text

    content = bsObj.find("div", {"id":"content"})
    ps = content.findAll("p")
    result['ps4']=ps[4].text

    bx2 = bsObj.find("div", {"class":"bx2"})
    result['bx2']=bx2.text

    return result

result = parse(pageString)
print(result['qtDayText2'])
print(result['ps4'])
print(result['bx2'])

res = finder.findBetween("민",3,5,13)
for re in res:
    print(re['index'], re['text'])
