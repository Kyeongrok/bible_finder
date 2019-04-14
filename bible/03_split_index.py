import json
import libs.bibleFinder as finder

def makeMessage(row):
    return "{} {}".format(row['index'], row['text'])

result = finder.findBetween("창",1, 2, 5)
for row in result:
    print(makeMessage(row))
    # print(row['chapter'])
print(len(result))
