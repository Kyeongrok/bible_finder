from service.remember.validator import validate
from service.remember.validator import list
import random
num = random.randrange(0, len(list))

validate(11, "딤후3:17", "이는 하나님의 사람으로 온전하게 하며 모든 선한 일을 행할 능력을 갖추게 하려 함이라")
validate(8, "빌4:6", "")

print("question->", num, list[num]['addr'])

