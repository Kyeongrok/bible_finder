from libs.crawler import crawl
from bs4 import BeautifulSoup

url = "http://www.365qt.com/TodaysQT.asp?QTID=7585"
pageString = crawl(url)
print(pageString)

bsObj = BeautifulSoup(pageString, "html.parser")
# print(bsObj)

qtDayText2 = bsObj.find("div", {"id":"qtDayText2"})
print(qtDayText2)

script = bsObj.find("div", {"class":"script"})
print(script)

content = bsObj.find("div", {"id":"content"})
ps = content.findAll("p")
print(ps[4])