from libs.remember.validator import validate
from libs.remember.validator import list
import random
num = random.randrange(0, len(list))

memo = [False] * len(list)
memo[9] = validate(9, "빌4:7", "그리하면 모든 지각에 뛰어난 하나님의 평강이 그리스도 예수 안에서 너희 마음과 생각을 지키시리라")
memo[4] = validate(4, "빌3:12", "")
print("question->", num, list[num]['addr'])
print(memo)

