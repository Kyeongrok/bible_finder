import libs.bibleFinder as finder
from libs.bibleMessageMaker import makeMessage

res = finder.findBetween("마",6,33,33)
print(makeMessage(res[0]))
