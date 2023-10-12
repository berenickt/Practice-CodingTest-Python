# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181900
"""
자열 my_string과 정수 배열 indices가 주어질 때,
my_string에서 indices의 원소에 해당하는 인덱스의 글자를 지우고 
이어 붙인 문자열을 return

입력#1
my_string : "apporoograpemmemprs"
indices   : [1, 16, 6, 15, 0, 10, 11, 3]

출력#1
"programmers"

📌 cf. enumerate()
인덱스(index)와 원소를 동시에 접근하면서 루프를 돌리고 싶을 떄
>>> for entry in enumerate(['A', 'B', 'C']):
...   print(entry)
(0, 'A')
(1, 'B')
(2, 'C')

📌 cf2. 포함(Containment) 연산자 
(in, not in) 제공하며, 객체 in (not in) 시퀀스의 형태로 사용 가능
"""


def solution(my_string, indices):
    l = [str for idx, str in enumerate(my_string) if idx not in indices]
    return "".join(l)


print(solution("apporoograpemmemprs", [1, 16, 6, 15, 0, 10, 11, 3]))
