import libs.bibleFinder as finder
from libs.bibleMessageMaker import makeMessage
from libs.htmlMaker import makeTable

res = finder.findBetween("민",3,5,13)

for re in res:
    print(re['index'], re['text'])

