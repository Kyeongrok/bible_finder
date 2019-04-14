import re
import os
from libs.jsonFileSaver import save
from libs.patternSplitter import split
import operator

pattern = "[가-힣]{1,2}[0-9]{1,3}:[0-9]{1,3} "
def fileToList(fileName):
    file = open(fileName)
    lines = file.readlines()

    result = []
    for line in lines:
        try:
            index = re.search(pattern, line).group(0).replace(" ", "")
            replaced = re.sub(pattern, "", line)
            splittedFileName = split(filename, "[0-9]{1}-[0-9]{2}")
            oldAndNew = int(splittedFileName[0].split("-")[0])
            chapter = int(splittedFileName[0].split("-")[1])
            bookName = splittedFileName[1].replace(".txt", "")
            splittedIndex = split(index, "[가-힣]{1,2}")
            statement = {"bookName":bookName,
                         "shortendBookName":splittedIndex[0], "oldAndNew":oldAndNew,
                         "chapter":int(splittedIndex[1].split(":")[0]),
                         "index":index,
                         "verse":int(index.split(":")[1]),
                         "text":replaced.replace("\n", "")}
            result.append(statement)
        except Exception as e:
            print(line)
            print("---error---", e)

    return result

result = []
for root, dirs, files in os.walk("./books/"):
    for filename in files:
        print(filename)
        lines = fileToList("./books/{}".format(filename))
        splittedFileName = split(filename, "[0-9]{1}-[0-9]{2}")
        oldAndNew = int(splittedFileName[0].split("-")[0])
        chapter = int(splittedFileName[0].split("-")[1])

        bookName = splittedFileName[1].replace(".txt", "")
        obj = {"bookName":bookName, "oldAndNew":oldAndNew, "lines":lines}
        result.append(obj)

lines = []
for ee in result:
    print(ee['bookName'])
    lines = lines + ee['lines']

save(lines, "./gaeLines.json")
