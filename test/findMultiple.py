import libs.bibleFinder as finder
from libs.bibleMessageMaker import makeMessage
from libs.htmlMaker import makeTable

res = finder.findBetween("마",6,33,33)
print(res[0])

print(makeMessage(res[0]))

table = makeTable(res)
print(table)

