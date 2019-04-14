import re

def split(text, pattern):
    index = re.search(pattern, text).group(0)
    replaced = re.sub(pattern, "", text)
    return [index, replaced]

