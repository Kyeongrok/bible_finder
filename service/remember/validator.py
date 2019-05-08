list = [
    {"week":1, "addr":"갈2:20", "text":"내가 그리스도와 함께 십자가에 못박혔나니 그런즉 이제는 내가 사는 것이 아니요 오직 내 안에 있는 그리스도께서 사시는 것이라 이제 내가 육체 가운데 사는 것은 나를 사랑하사 나를 위해 자기 자신을 버리신 하나님의 아들을 믿는 믿음 안에서 사는 것이라."},
    {"week":1, "addr":"마16:24-25", "text":"누구든지 제 목숨을 구원하고자 하면 잃을 것이요 누구든지 나를 위하여 제 목숨을 잃으면 찾으리라"},
    {"week":2, "addr":"엡4:15", "text":"오직 사랑 안에서 참된 것을 하여 범사에 그에게까지 자랄지라 그는 머리니 곧 그리스도라"},
    {"week":2, "addr":"빌3:12", "text":"내가 이미 얻었다 함도 아니요 온전히 이루었다 함도 아니라 오직 내가 그리스도 예수께 잡힌바 된 그것을 잡으려고 달려가노라"},
    {"week":3, "addr":"마4:4", "text":"예수께서 대답하여 이르시되 기록되었으되 사람이 떡으로만 살 것이 아니요 하나님의 입으로부터 나오는 모든 말씀으로 살 것이라 하였느니라 하시니"},
    {"week":3, "addr":"수1:8", "text":"이 율법책을 네 입에서 떠나지 말게 하며 주야로 그것을 묵상하여 그 안에 기록된 대로 다 지켜 행하라 그리하면 네 길이 평탄하게 될 것이며 네가 형통하리라"},
    {"week":4, "addr":"마6:33", "text":"그런즉 너희는 먼저 그의 나라와 그 의를 구하라 그리하면 이 모든 것을 너희에게 더하시리라"},
    {"week":4, "addr":"빌4:6", "text":"아무 것도 염려하지 말고 다만 모든 일에 기도와 간구로 너희 구할 것을 감사함으로 하나님께 아뢰라"},
    {"week":4, "addr":"빌4:7", "text":"그리하면 모든 지각에 뛰어난 하나님의 평강이 그리스도 예수 안에서 너희 마음과 생각을 지키시리라"},
    {"week":5, "addr":"딤후3:16-17", "text":"모든 성경은 하나님의 감동으로 된 것으로 교훈과 책망과 바르게 함과 의로 교육하기에 유익하니 이는 하나님의 사람으로 온전하게 하며 모든 선한 일을 행할 능력을 갖추게 하려 함이라"},
    {"week":5, "addr":"시119:33", "text":"여호와여 주의 율례들의 도를 내게 가르치소서 내가 끝까지 지키리이다"},
]

def validate(num, addr, answer):
    if(list[num]['addr'] == addr and list[num]['text'] == answer):
        print("{} {} pass".format(num, addr))
        return True
    else:
        print("fail {} {}", addr, list[num]['text'])
        return False
