import json

file = open("./gaeLines.json")
bible = json.loads(file.read())


def findByIndex(index):
    result = list(filter(lambda x: x['index']==index, bible))
    return result

def findBetween(shortendBookName, chapter, verseFrom, verseTo):
    result = list(filter(lambda x: (x['shortendBookName']==shortendBookName
                         and x['chapter'] == chapter
                         and x['verse'] >= verseFrom
                        and x['verse'] <= verseTo
                                    )
                         , bible))
    return result

